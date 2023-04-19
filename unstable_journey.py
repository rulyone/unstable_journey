from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6 import QtGui, QtWidgets, QtCore

from PySide6.QtGui import QPainter, QBitmap, QPolygon, QPen, QBrush, QColor, QGuiApplication
from PySide6.QtCore import Qt, QCoreApplication

from MainWindow import Ui_MainWindow

from Worker import Worker
from os.path import expanduser
from os import makedirs, path
import random
import time

import webuiapi
import logging
import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
from PIL.ImageQt import ImageQt
from PIL.PngImagePlugin import PngInfo



import os
import sys
import random
import types

# Set the application name and version
QCoreApplication.setApplicationName("MyApp")
QCoreApplication.setApplicationVersion("1.0")

# Generate the AppUserModelID
myappid = f"com.learnpyqt.minute-apps.{QCoreApplication.applicationName()}-{QCoreApplication.applicationVersion()}"

# Set the AppUserModelID
QGuiApplication.setApplicationDisplayName(myappid)

BRUSH_MULT = 3
SPRAY_PAINT_MULT = 5
SPRAY_PAINT_N = 100

COLORS = [
    '#000000', '#82817f', '#820300', '#868417', '#007e03', '#037e7b', '#040079',
    '#81067a', '#7f7e45', '#05403c', '#0a7cf6', '#093c7e', '#7e07f9', '#7c4002',

    '#ffffff', '#c1c1c1', '#f70406', '#fffd00', '#08fb01', '#0bf8ee', '#0000fa',
    '#b92fc2', '#fffc91', '#00fd83', '#87f9f9', '#8481c4', '#dc137d', '#fb803c',
]

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]

MODES = [
    #'selectpoly', 'polyline', 'polygon', 'text'
    'selectrect',
    'eraser', 'fill',
    'dropper', 'stamp',
    'pen', 'brush',
    'spray',
    'line',
    'rect',
    'ellipse', 'roundrect'
]

CANVAS_DIMENSIONS = 512, 512

STAMPS = [
    ':/stamps/unstable_journey_logo.ico',
    ':/stamps/pie-apple.png',
    ':/stamps/pie-cherry.png',
    ':/stamps/pie-cherry2.png',
    ':/stamps/pie-lemon.png',
    ':/stamps/pie-moon.png',
    ':/stamps/pie-pork.png',
    ':/stamps/pie-pumpkin.png',
    ':/stamps/pie-walnut.png'
]

SELECTION_PEN = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.DashLine)
PREVIEW_PEN = QPen(QColor(0xff, 0xff, 0xff), 1, Qt.SolidLine)


def build_font(config):
    """
    Construct a complete font from the configuration options
    :param self:
    :param config:
    :return: QFont
    """
    font = config['font']
    font.setPointSize(config['fontsize'])
    font.setBold(config['bold'])
    font.setItalic(config['italic'])
    font.setUnderline(config['underline'])
    return font

class SDCanvas(QLabel):

    primary_color = QColor(Qt.black)
    secondary_color = None

    def initialize(self):
        self.background_color = QColor(self.secondary_color) if self.secondary_color else QColor(Qt.white)
        self.reset()

    def reset(self):
        # Create the pixmap for display.
        pixmap_copy = QPixmap(*CANVAS_DIMENSIONS)

        # Clear the canvas.
        pixmap_copy.fill(self.background_color)
        self.setPixmap(pixmap_copy)
    

class Canvas(QLabel):

    mode = 'rectangle'

    primary_color = QColor(Qt.black)
    secondary_color = None

    primary_color_updated = Signal(str)
    secondary_color_updated = Signal(str)

    # Store configuration settings, including pen width, fonts etc.
    config = {
        # Drawing options.
        'size': 1,
        'fill': True,
        # Font options.
        'font': QFont('Times'),
        'fontsize': 12,
        'bold': False,
        'italic': False,
        'underline': False,
    }

    active_color = None
    preview_pen = None

    timer_event = None

    current_stamp = None

    def initialize(self):
        self.lastPressure = None
        self.background_color = QColor(self.secondary_color) if self.secondary_color else QColor(Qt.white)
        self.eraser_color = QColor(self.secondary_color) if self.secondary_color else QColor(Qt.white)
        self.eraser_color.setAlpha(100)
        self.reset()
        self.threadpool = QThreadPool.globalInstance()
        self.symmetryActive = False

    def reset(self):
        # Create the pixmap for display.
        pixmap_copy = QPixmap(*CANVAS_DIMENSIONS)

        # Clear the canvas.
        pixmap_copy.fill(self.background_color)
        self.setPixmap(pixmap_copy)

    def set_primary_color(self, hex):
        self.primary_color = QColor(hex)

    def set_secondary_color(self, hex):
        self.secondary_color = QColor(hex)

    def set_config(self, key, value):
        self.config[key] = value

    def set_mode(self, mode):
        # Clean up active timer animations.
        self.timer_cleanup()
        # Reset mode-specific vars (all)
        self.active_shape_fn = None
        self.active_shape_args = ()

        self.origin_pos = None

        self.current_pos = None
        self.last_pos = None

        self.history_pos = None
        self.last_history = []

        self.current_text = ""
        self.last_text = ""

        self.last_config = {}

        self.dash_offset = 0
        self.locked = False
        # Apply the mode
        self.mode = mode

    def reset_mode(self):
        self.set_mode(self.mode)

    def on_timer(self):
        if self.timer_event:
            self.timer_event()

    def timer_cleanup(self):
        if self.timer_event:
            # Stop the timer, then trigger cleanup.
            timer_event = self.timer_event
            self.timer_event = None
            timer_event(final=True)


    # Tablet events.

    def tabletEvent(self, e):
        self.lastPressure = e.pressure()

    # Mouse events.

    def mousePressEvent(self, e):
        fn = getattr(self, "%s_mousePressEvent" % self.mode, None)
        if fn:
            return fn(e)

    def mouseMoveEvent(self, e):
        fn = getattr(self, "%s_mouseMoveEvent" % self.mode, None)
        if fn:
            return fn(e)

    def mouseReleaseEvent(self, e):
        fn = getattr(self, "%s_mouseReleaseEvent" % self.mode, None)
        if fn:
            return fn(e)

    def mouseDoubleClickEvent(self, e):
        fn = getattr(self, "%s_mouseDoubleClickEvent" % self.mode, None)
        if fn:
            return fn(e)

    # Generic events (shared by brush-like tools)

    def generic_mousePressEvent(self, e):
        self.last_pos = e.position()

        if e.button() == Qt.LeftButton:
            self.active_color = self.primary_color
        else:
            self.active_color = self.secondary_color

    def generic_mouseReleaseEvent(self, e):
        self.last_pos = None

    # Mode-specific events.

    # # Select polygon events

    # def selectpoly_mousePressEvent(self, e):
    #     if not self.locked or e.button == Qt.RightButton:
    #         self.active_shape_fn = 'drawPolygon'
    #         self.preview_pen = SELECTION_PEN
    #         self.generic_poly_mousePressEvent(e)

    # def selectpoly_timerEvent(self, final=False):
    #     self.generic_poly_timerEvent(final)

    # def selectpoly_mouseMoveEvent(self, e):
    #     if not self.locked:
    #         self.generic_poly_mouseMoveEvent(e)

    # def selectpoly_mouseDoubleClickEvent(self, e):
    #     self.current_pos = e.pos()
    #     self.locked = True

    # def selectpoly_copy(self):
    #     """
    #     Copy a polygon region from the current image, returning it.

    #     Create a mask for the selected area, and use it to blank
    #     out non-selected regions. Then get the bounding rect of the
    #     selection and crop to produce the smallest possible image.

    #     :return: QPixmap of the copied region.
    #     """
    #     self.timer_cleanup()

    #     pixmap = self.pixmap().copy()
    #     bitmap = QBitmap(*CANVAS_DIMENSIONS)
    #     bitmap.clear()  # Starts with random data visible.

    #     p = QPainter(bitmap)
    #     # Construct a mask where the user selected area will be kept, 
    #     # the rest removed from the image is transparent.
    #     userpoly = QPolygon(self.history_pos + [self.current_pos])
    #     p.setPen(QPen(Qt.color1))
    #     p.setBrush(QBrush(Qt.color1))  # Solid color, Qt.color1 == bit on.
    #     p.drawPolygon(userpoly)
    #     p.end()

    #     # Set our created mask on the image.
    #     pixmap.setMask(bitmap)

    #     # Calculate the bounding rect and return a copy of that region.
    #     return pixmap.copy(userpoly.boundingRect())

    # Select rectangle events

    def selectrect_mousePressEvent(self, e):
        self.active_shape_fn = 'drawRect'
        self.preview_pen = SELECTION_PEN
        self.generic_shape_mousePressEvent(e)

    def selectrect_timerEvent(self, final=False):
        self.generic_shape_timerEvent(final)

    def selectrect_mouseMoveEvent(self, e):
        if not self.locked:
            self.current_pos = e.pos()

    def selectrect_mouseReleaseEvent(self, e):
        self.current_pos = e.pos()
        self.locked = True

    def selectrect_copy(self):
        """
        Copy a rectangle region of the current image, returning it.

        :return: QPixmap of the copied region.
        """
        self.timer_cleanup()
        return self.pixmap().copy(QRect(self.origin_pos, self.current_pos))

    # Eraser events

    def eraser_mousePressEvent(self, e):
        self.generic_mousePressEvent(e)

    def eraser_mouseMoveEvent(self, e):
        if self.last_pos:
            pixmap_copy = self.pixmap()
            p = QPainter(pixmap_copy)
            p.setPen(QPen(self.eraser_color, 30, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawLine(self.last_pos, e.pos())
            p.end()
            self.setPixmap(pixmap_copy)
            self.last_pos = e.pos()
            #self.update()

    def eraser_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    # Stamp (pie) events

    def stamp_mousePressEvent(self, e):
        pixmap_copy = self.pixmap()
        p = QPainter(pixmap_copy)
        stamp = self.current_stamp
        p.drawPixmap(e.x() - stamp.width() // 2, e.y() - stamp.height() // 2, stamp)
        p.end()
        self.setPixmap(pixmap_copy)
        #self.update()

    # Pen events

    def pen_mousePressEvent(self, e):
        self.generic_mousePressEvent(e)

    def pen_mouseMoveEvent(self, e):
        
        if self.last_pos:
            pen_width = self.config['size']
            if self.symmetryActive:
                mirror_last_pos = QPoint(self.pixmap().width() - self.last_pos.x(), self.last_pos.y())
                mirror_pos = QPoint(self.pixmap().width() - e.x(), e.y())
            if self.lastPressure is not None:
                 pen_width = pen_width * self.lastPressure
                
            pixmap_copy = self.pixmap()
            p = QPainter(pixmap_copy)
            p.setPen(QPen(self.active_color, pen_width, Qt.SolidLine, Qt.SquareCap, Qt.RoundJoin))
            p.drawLine(self.last_pos, e.pos())
            if self.symmetryActive:
                p.drawLine(mirror_last_pos, mirror_pos)
            p.end()
            self.setPixmap(pixmap_copy)
            self.update()
            self.last_pos = e.pos()

    def pen_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    # Brush events

    def brush_mousePressEvent(self, e):
        self.generic_mousePressEvent(e)

    def brush_mouseMoveEvent(self, e):
        if self.last_pos:
            pen_width = self.config['size']
            if self.symmetryActive:
                mirror_last_pos = QPoint(self.pixmap().width() - self.last_pos.x(), self.last_pos.y())
                mirror_pos = QPoint(self.pixmap().width() - e.x(), e.y())
            if self.lastPressure is not None:
                 pen_width = pen_width * self.lastPressure

            pixmap_copy = self.pixmap()
            p = QPainter(pixmap_copy)
            p.setPen(QPen(self.active_color, pen_width * BRUSH_MULT, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawLine(self.last_pos, e.pos())
            if self.symmetryActive:
                p.drawLine(mirror_last_pos, mirror_pos)
            p.end()
            self.setPixmap(pixmap_copy)
            self.update()
            self.last_pos = e.pos()
            
    def brush_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    # Spray events

    def spray_mousePressEvent(self, e):
        self.generic_mousePressEvent(e)

    def spray_mouseMoveEvent(self, e):
        if self.last_pos:
            pen_width = self.config['size']
            if self.symmetryActive:
                mirror_pos = QPoint(self.pixmap().width() - e.x(), e.y())
            if self.lastPressure is not None:
                 pen_width = pen_width * self.lastPressure
                 
            pixmap_copy = self.pixmap()
            p = QPainter(pixmap_copy)
            p.setPen(QPen(self.active_color, pen_width))

            for n in range(self.config['size'] * SPRAY_PAINT_N):
                xo = random.gauss(0, self.config['size'] * SPRAY_PAINT_MULT)
                yo = random.gauss(0, self.config['size'] * SPRAY_PAINT_MULT)
                p.drawPoint(QPointF(e.x() + xo, e.y() + yo))
                if self.symmetryActive:
                    p.drawPoint(QPointF(mirror_pos.x() + xo, mirror_pos.y() + yo))
            p.end()
            self.setPixmap(pixmap_copy)

            self.update()

    def spray_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    # Text events

    def keyPressEvent(self, e):
        if self.mode == 'text':
            if e.key() == Qt.Key_Backspace:
                self.current_text = self.current_text[:-1]
            else:
                self.current_text = self.current_text + e.text()

    def text_mousePressEvent(self, e):
        if e.button() == Qt.LeftButton and self.current_pos is None:
            self.current_pos = e.pos()
            self.current_text = ""
            self.timer_event = self.text_timerEvent

        elif e.button() == Qt.LeftButton:

            self.timer_cleanup()
            # Draw the text to the image
            pixmap_copy = self.pixmap()
            p = QPainter(pixmap_copy)
            p.setRenderHints(QPainter.Antialiasing)
            font = build_font(self.config)
            p.setFont(font)
            pen = QPen(self.primary_color, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            p.setPen(pen)
            p.drawText(self.current_pos, self.current_text)
            p.end()
            self.setPixmap(pixmap_copy)
            self.update()

            self.reset_mode()

        elif e.button() == Qt.RightButton and self.current_pos:
            self.reset_mode()

    def text_timerEvent(self, final=False):
        pixmap_copy = self.pixmap()
        p = QPainter(pixmap_copy)
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = PREVIEW_PEN
        p.setPen(pen)
        if self.last_text:
            font = build_font(self.last_config)
            p.setFont(font)
            p.drawText(self.current_pos, self.last_text)

        if not final:
            font = build_font(self.config)
            p.setFont(font)
            p.drawText(self.current_pos, self.current_text)
        p.end()
        self.setPixmap(pixmap_copy)

        self.last_text = self.current_text
        self.last_config = self.config.copy()
        self.update()

    # Fill events

    def fill_mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            self.active_color = self.primary_color
        else:
            self.active_color = self.secondary_color

        image = self.pixmap().toImage()
        w, h = image.width(), image.height()
        x, y = e.x(), e.y()

        # Get our target color from origin.
        target_color = image.pixel(x,y)

        have_seen = set()
        queue = [(x, y)]

        def get_cardinal_points(have_seen, center_pos):
            points = []
            cx, cy = center_pos
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = cx + x, cy + y
                if (xx >= 0 and xx < w and
                    yy >= 0 and yy < h and
                    (xx, yy) not in have_seen):

                    points.append((xx, yy))
                    have_seen.add((xx, yy))

            return points

        # Now perform the search and fill.
        pixmap_copy = self.pixmap()
        p = QPainter(pixmap_copy)
        p.setPen(QPen(self.active_color))

        while queue:
            x, y = queue.pop()
            if image.pixel(x, y) == target_color:
                p.drawPoint(QPoint(x, y))
                queue.extend(get_cardinal_points(have_seen, (x, y)))
        p.end()
        self.setPixmap(pixmap_copy)
        self.update()

    # Dropper events

    def dropper_mousePressEvent(self, e):
        c = self.pixmap().toImage().pixel(e.pos())
        hex = QColor(c).name()

        if e.button() == Qt.LeftButton:
            self.set_primary_color(hex)
            self.primary_color_updated.emit(hex)  # Update UI.

        elif e.button() == Qt.RightButton:
            self.set_secondary_color(hex)
            self.secondary_color_updated.emit(hex)  # Update UI.

    # Generic shape events: Rectangle, Ellipse, Rounded-rect

    def generic_shape_mousePressEvent(self, e):
        self.origin_pos = e.pos()
        self.current_pos = e.pos()
        self.timer_event = self.generic_shape_timerEvent

    def generic_shape_timerEvent(self, final=False):
        pixmap_copy = self.pixmap()
        p = QPainter(pixmap_copy)
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = self.preview_pen
        pen.setDashOffset(self.dash_offset)
        p.setPen(pen)
        if self.last_pos:
            getattr(p, self.active_shape_fn)(QRect(self.origin_pos, self.last_pos), *self.active_shape_args)

        if not final:
            self.dash_offset -= 1
            pen.setDashOffset(self.dash_offset)
            p.setPen(pen)
            getattr(p, self.active_shape_fn)(QRect(self.origin_pos, self.current_pos), *self.active_shape_args)
        p.end()
        self.setPixmap(pixmap_copy)
        self.update()
        self.last_pos = self.current_pos

    def generic_shape_mouseMoveEvent(self, e):
        self.current_pos = e.pos()

    def generic_shape_mouseReleaseEvent(self, e):
        if self.last_pos:
            # Clear up indicator.
            self.timer_cleanup()

            pixmap_copy = self.pixmap()
            p = QPainter(pixmap_copy)
            p.setPen(QPen(self.primary_color, self.config['size'], Qt.SolidLine, Qt.SquareCap, Qt.MiterJoin))

            if self.config['fill']:
                p.setBrush(QBrush(self.secondary_color))
            getattr(p, self.active_shape_fn)(QRect(self.origin_pos, e.pos()), *self.active_shape_args)
            p.end()
            self.setPixmap(pixmap_copy)
            self.update()

        self.reset_mode()

    # Line events

    def line_mousePressEvent(self, e):
        self.origin_pos = e.pos()
        self.current_pos = e.pos()
        self.preview_pen = PREVIEW_PEN
        self.timer_event = self.line_timerEvent

    def line_timerEvent(self, final=False):
        pixmap_copy = self.pixmap()
        p = QPainter(pixmap_copy)
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = self.preview_pen
        p.setPen(pen)
        if self.last_pos:
            p.drawLine(self.origin_pos, self.last_pos)

        if not final:
            p.drawLine(self.origin_pos, self.current_pos)
        p.end()
        self.setPixmap(pixmap_copy)
        self.update()
        self.last_pos = self.current_pos

    def line_mouseMoveEvent(self, e):
        self.current_pos = e.pos()

    def line_mouseReleaseEvent(self, e):
        if self.last_pos:
            # Clear up indicator.
            self.timer_cleanup()

            pixmap_copy = self.pixmap()
            p = QPainter(pixmap_copy)
            p.setPen(QPen(self.primary_color, self.config['size'], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            p.drawLine(self.origin_pos, e.pos())
            p.end()
            self.setPixmap(pixmap_copy)
            self.update()

        self.reset_mode()

    """ # Generic poly events
    def generic_poly_mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.history_pos:
                self.history_pos.append(e.pos())
            else:
                self.history_pos = [e.pos()]
                self.current_pos = e.pos()
                self.timer_event = self.generic_poly_timerEvent

        elif e.button() == Qt.RightButton and self.history_pos:
            # Clean up, we're not drawing
            self.timer_cleanup()
            self.reset_mode()

    def generic_poly_timerEvent(self, final=False):
        pixmap_copy = self.pixmap()
        p = QPainter(pixmap_copy)
        p.setCompositionMode(QPainter.RasterOp_SourceXorDestination)
        pen = self.preview_pen
        pen.setDashOffset(self.dash_offset)
        p.setPen(pen)
        if self.last_history:
            getattr(p, self.active_shape_fn)(*self.last_history)

        if not final:
            self.dash_offset -= 1
            pen.setDashOffset(self.dash_offset)
            p.setPen(pen)
            getattr(p, self.active_shape_fn)(*self.history_pos + [self.current_pos])
        p.end()
        self.setPixmap(pixmap_copy)
        self.update()
        self.last_pos = self.current_pos
        self.last_history = self.history_pos + [self.current_pos]

    def generic_poly_mouseMoveEvent(self, e):
        self.current_pos = e.pos()

    def generic_poly_mouseDoubleClickEvent(self, e):
        self.timer_cleanup()
        pixmap_copy = self.pixmap()
        p = QPainter(pixmap_copy)
        p.setPen(QPen(self.primary_color, self.config['size'], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

        # Note the brush is ignored for polylines.
        if self.secondary_color:
            p.setBrush(QBrush(self.secondary_color))

        getattr(p, self.active_shape_fn)(*self.history_pos + [e.pos()])

        p.end()
        self.setPixmap(pixmap_copy)
        self.update()
        self.reset_mode()

    # Polyline events

    def polyline_mousePressEvent(self, e):
        self.active_shape_fn = 'drawPolyline'
        self.preview_pen = PREVIEW_PEN
        self.generic_poly_mousePressEvent(e)

    def polyline_timerEvent(self, final=False):
        self.generic_poly_timerEvent(final)

    def polyline_mouseMoveEvent(self, e):
        self.generic_poly_mouseMoveEvent(e)

    def polyline_mouseDoubleClickEvent(self, e):
        self.generic_poly_mouseDoubleClickEvent(e)

    # Rectangle events

    def rect_mousePressEvent(self, e):
        self.active_shape_fn = 'drawRect'
        self.active_shape_args = ()
        self.preview_pen = PREVIEW_PEN
        self.generic_shape_mousePressEvent(e)

    def rect_timerEvent(self, final=False):
        self.generic_shape_timerEvent(final)

    def rect_mouseMoveEvent(self, e):
        self.generic_shape_mouseMoveEvent(e)

    def rect_mouseReleaseEvent(self, e):
        self.generic_shape_mouseReleaseEvent(e)

    # Polygon events

    def polygon_mousePressEvent(self, e):
        self.active_shape_fn = 'drawPolygon'
        self.preview_pen = PREVIEW_PEN
        self.generic_poly_mousePressEvent(e)

    def polygon_timerEvent(self, final=False):
        self.generic_poly_timerEvent(final)

    def polygon_mouseMoveEvent(self, e):
        self.generic_poly_mouseMoveEvent(e)

    def polygon_mouseDoubleClickEvent(self, e):
        self.generic_poly_mouseDoubleClickEvent(e) """

    # Ellipse events

    def ellipse_mousePressEvent(self, e):
        self.active_shape_fn = 'drawEllipse'
        self.active_shape_args = ()
        self.preview_pen = PREVIEW_PEN
        self.generic_shape_mousePressEvent(e)

    def ellipse_timerEvent(self, final=False):
        self.generic_shape_timerEvent(final)

    def ellipse_mouseMoveEvent(self, e):
        self.generic_shape_mouseMoveEvent(e)

    def ellipse_mouseReleaseEvent(self, e):
        self.generic_shape_mouseReleaseEvent(e)

    # Roundedrect events

    def roundrect_mousePressEvent(self, e):
        self.active_shape_fn = 'drawRoundedRect'
        self.active_shape_args = (25, 25)
        self.preview_pen = PREVIEW_PEN
        self.generic_shape_mousePressEvent(e)

    def roundrect_timerEvent(self, final=False):
        self.generic_shape_timerEvent(final)

    def roundrect_mouseMoveEvent(self, e):
        self.generic_shape_mouseMoveEvent(e)

    def roundrect_mouseReleaseEvent(self, e):
        self.generic_shape_mouseReleaseEvent(e)

def deleteItemsOfLayout(layout):
     if layout is not None:
         while layout.count():
             item = layout.takeAt(0)
             widget = item.widget()
             if widget is not None:
                 widget.setParent(None)
             else:
                 deleteItemsOfLayout(item.layout())

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):

        # create API client with custom host, port
        self.use_https = False
        self.api = webuiapi.WebUIApi(host='localhost', port=7860, use_https=self.use_https)
        self.cn_interface = webuiapi.ControlNetInterface(self.api)
        #print(self.cn_interface.model_list())
        #self.api.set_auth('test', 'test123')

        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Replace canvas placeholder from QtDesigner.
        self.horizontalLayout.removeWidget(self.canvas)
        self.canvas = Canvas()
        self.canvas.initialize()
        # We need to enable mouse tracking to follow the mouse without the button pressed.
        self.canvas.setMouseTracking(True)
        # Enable focus to capture key inputs.
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.horizontalLayout.addWidget(self.canvas)

        # Setup the stable diffusion vertical layout actions again (because we removed previous canvas)
        for i in range(self.horizontalLayout.count()):
            layout_item = self.horizontalLayout.itemAt(i)
            if layout_item.layout() == self.verticalLayout_4:
                #deleteItemsOfLayout(layout_item.layout())
                self.horizontalLayout.removeItem(layout_item)
                break
        
        self.horizontalLayout.addLayout(self.verticalLayout_4)

        # Setup the stable diffusion canvas again (because we removed previously canvas and vertical layout)
        self.horizontalLayout.removeWidget(self.sdCanvas)
        self.sdCanvas = SDCanvas()
        self.sdCanvas.initialize()
        self.horizontalLayout.addWidget(self.sdCanvas)

        # Setup stable diffusion inputs
        seedValidator = QIntValidator(self)
        self.seedLineEdit.setValidator(seedValidator)

        self.portLineEdit.setValidator(seedValidator)
        
        samplers = ['Euler a', 'Euler', 'LMS', 'Heun', 
                    'DPM2', 'DPM2 a', 'DPM++ 2S a', 'DPM++ 2M', 'DPM++ SDE', 'DPM fast', 'DPM adaptive', 
                    'LMS Karras', 'DPM2 Karras', 'DPM2 a Karras', 'DPM++ 2S a Karras', 'DPM++ 2M Karras', 'DPM++ SDE Karras',
                    'DDIM', 'PLMS', 'UniPC']
        
        for sampler in samplers:
            self.samplerComboBox.addItem(sampler, sampler)

        self.cnModelComboBox.addItem('none', 'none')
        self.cnPreComboBox.addItem('none', 'none')

        self.cnSelectedModel = None
        self.cnSelectedModule = None

        # Setup the mode buttons
        self.mode_group = QButtonGroup(self)
        self.mode_group.setExclusive(True)

        for mode in MODES:
            btn = getattr(self, '%sButton' % mode)
            btn.pressed.connect(lambda mode=mode: self.canvas.set_mode(mode))
            self.mode_group.addButton(btn)

        self.mode_group.buttonClicked.connect(self.mode_groupClicked)

        # Setup the SD inputs
        self.convertSDButton.clicked.connect(self.convertCanvasToSD)
        self.replaceSDButton.clicked.connect(self.replaceCanvasFromSD)
        self.seedRandomizeButton.clicked.connect(self.randomizeSeed)

        self.refreshModelButton.clicked.connect(self.refreshModel)
        self.modelComboBox.currentTextChanged.connect(self.modelComboBoxChanged)

        self.refreshCNModelButton.clicked.connect(self.refreshCNModel)
        self.cnModelComboBox.currentTextChanged.connect(self.cnModelComboBoxChanged)
        self.cnPreComboBox.currentTextChanged.connect(self.cnPreComboBoxChanged)

        self.helpPushButton.clicked.connect(self.showHelp)

        self.hostLineEdit.textChanged.connect(self.hostOrPortChanged)
        self.portLineEdit.textChanged.connect(self.hostOrPortChanged)

        self.httpsCheckBox.stateChanged.connect(self.httpsChanged)

        self.symmetryButton.toggled.connect(self.symmetryToggled)

        # Setup the color selection buttons.
        self.primaryButton.pressed.connect(lambda: self.choose_color(self.set_primary_color))
        self.secondaryButton.pressed.connect(lambda: self.choose_color(self.set_secondary_color))

        # Initialize button colours.
        for n, hex in enumerate(COLORS, 1):
            btn = getattr(self, 'colorButton_%d' % n)
            btn.setStyleSheet('QPushButton { background-color: %s; }' % hex)
            btn.hex = hex  # For use in the event below

            def patch_mousePressEvent(self_, e):
                if e.button() == Qt.LeftButton:
                    self.set_primary_color(self_.hex)

                elif e.button() == Qt.RightButton:
                    self.set_secondary_color(self_.hex)

            btn.mousePressEvent = types.MethodType(patch_mousePressEvent, btn)

        # Setup up action signals
        self.actionCopy.triggered.connect(self.copy_to_clipboard)

        # Initialize animation timer.
        self.timer = QTimer()
        self.timer.timeout.connect(self.canvas.on_timer)
        self.timer.setInterval(100)
        self.timer.start()

        # Setup to agree with Canvas.
        self.set_primary_color('#000000')
        self.set_secondary_color('#ffffff')

        # Signals for canvas-initiated color changes (dropper).
        self.canvas.primary_color_updated.connect(self.set_primary_color)
        self.canvas.secondary_color_updated.connect(self.set_secondary_color)

        # Setup the stamp state.
        self.current_stamp_n = -1
        self.next_stamp()
        self.stampnextButton.pressed.connect(self.next_stamp)

        # Menu options
        self.actionNewImage.triggered.connect(self.new_image)
        self.actionOpenImage.triggered.connect(self.open_file)
        self.actionSaveImage.triggered.connect(self.save_file)
        self.actionClearImage.triggered.connect(self.canvas.reset)
        self.actionInvertColors.triggered.connect(self.invert)
        self.actionFlipHorizontal.triggered.connect(self.flip_horizontal)
        self.actionFlipVertical.triggered.connect(self.flip_vertical)

        # Setup the drawing toolbar.
        self.fontselect = QFontComboBox()
        #self.fontToolbar.addWidget(self.fontselect)
        self.fontselect.currentFontChanged.connect(lambda f: self.canvas.set_config('font', f))
        self.fontselect.setCurrentFont(QFont('Times'))

        self.fontsize = QComboBox()
        self.fontsize.addItems([str(s) for s in FONT_SIZES])
        self.fontsize.currentTextChanged.connect(lambda f: self.canvas.set_config('fontsize', int(f)))

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        #self.fontToolbar.addWidget(self.fontsize)

        #self.fontToolbar.addAction(self.actionBold)
        # self.actionBold.triggered.connect(lambda s: self.canvas.set_config('bold', s))
        # self.fontToolbar.addAction(self.actionItalic)
        # self.actionItalic.triggered.connect(lambda s: self.canvas.set_config('italic', s))
        # self.fontToolbar.addAction(self.actionUnderline)
        # self.actionUnderline.triggered.connect(lambda s: self.canvas.set_config('underline', s))

        sizeicon = QLabel()
        sizeicon.setPixmap(QPixmap(':/icons/border-weight.png'))
        self.drawingToolbar.addWidget(sizeicon)
        self.sizeselect = QSlider()
        self.sizeselect.setRange(1,20)
        self.sizeselect.setOrientation(Qt.Horizontal)
        self.sizeselect.valueChanged.connect(lambda s: self.canvas.set_config('size', s))
        self.drawingToolbar.addWidget(self.sizeselect)

        self.actionFillShapes.triggered.connect(lambda s: self.canvas.set_config('fill', s))
        self.drawingToolbar.addAction(self.actionFillShapes)
        self.actionFillShapes.setChecked(True)

        self.show()

    def choose_color(self, callback):
        dlg = QColorDialog()
        if dlg.exec():
            callback( dlg.selectedColor().name() )

    def set_primary_color(self, hex):
        self.canvas.set_primary_color(hex)
        self.primaryButton.setStyleSheet('QPushButton { background-color: %s; }' % hex)

    def set_secondary_color(self, hex):
        self.canvas.set_secondary_color(hex)
        self.secondaryButton.setStyleSheet('QPushButton { background-color: %s; }' % hex)

    def next_stamp(self):
        self.current_stamp_n += 1
        if self.current_stamp_n >= len(STAMPS):
            self.current_stamp_n = 0

        pixmap = QPixmap(STAMPS[self.current_stamp_n])
        self.stampnextButton.setIcon(QIcon(pixmap))

        self.canvas.current_stamp = pixmap

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()

        if self.canvas.mode == 'selectrect' and self.canvas.locked:
            clipboard.setPixmap(self.canvas.selectrect_copy())

        elif self.canvas.mode == 'selectpoly' and self.canvas.locked:
            clipboard.setPixmap(self.canvas.selectpoly_copy())

        else:
            clipboard.setPixmap(self.canvas.pixmap())

    def new_image(self):
        self.canvas.initialize()
        self.canvas.symmetryActive = self.symmetryButton.isChecked()

    def open_file(self):
        """
        Open image file for editing, scaling the smaller dimension and cropping the remainder.
        :return:
        """
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "PNG image files (*.png); JPEG image files (*jpg); All files (*.*)")

        if path:
            pixmap = QPixmap()
            pixmap.load(path)

            # We need to crop down to the size of our canvas. Get the size of the loaded image.
            iw = pixmap.width()
            ih = pixmap.height()

            # Get the size of the space we're filling.
            cw, ch = CANVAS_DIMENSIONS

            if iw/cw < ih/ch:  # The height is relatively bigger than the width.
                pixmap = pixmap.scaledToWidth(cw)
                hoff = (pixmap.height() - ch) // 2
                pixmap = pixmap.copy(
                    QRect(QPoint(0, hoff), QPoint(cw, pixmap.height()-hoff))
                )

            elif iw/cw > ih/ch:  # The height is relatively bigger than the width.
                pixmap = pixmap.scaledToHeight(ch)
                woff = (pixmap.width() - cw) // 2
                pixmap = pixmap.copy(
                    QRect(QPoint(woff, 0), QPoint(pixmap.width()-woff, ch))
                )

            self.canvas.setPixmap(pixmap)

    def randomizeSeed(self):
        # based on https://www.reddit.com/r/StableDiffusion/comments/yiqeiy/silly_question_how_many_seeds_exist_in_stable/
        self.seedLineEdit.setText(str(random.randint(0, sys.maxsize)))

    def hostOrPortChanged(self):
        self.api = webuiapi.WebUIApi(host=self.hostLineEdit.text(), port=int(self.portLineEdit.text()), use_https=self.use_https)
        self.cn_interface = webuiapi.ControlNetInterface(self.api)

    def httpsChanged(self, state):
        if Qt.CheckState(state) == Qt.CheckState.Checked:
            self.use_https = True 
        else:
            self.use_https = False
        self.api = webuiapi.WebUIApi(host=self.hostLineEdit.text(), port=int(self.portLineEdit.text()), use_https=self.use_https)
        self.cn_interface = webuiapi.ControlNetInterface(self.api)

    def mode_groupClicked(self, info):
        if info.objectName() not in ['brushButton', 'sprayButton', 'penButton'] and self.symmetryButton.isChecked():
            msg = QMessageBox()
            msg.setIconPixmap(QPixmap(':/icons/unstable_journey_logo.ico'))
            msg.setText("Symmetry mode disabled")
            msg.setInformativeText("Symmetry mode works only with Brush, Pen or Spray modes at the moment.")
            msg.setWindowTitle("Info")
            msg.exec()
            self.symmetryButton.toggle()
        
    def symmetryToggled(self, toggle):
        if toggle:
            #we can only use this mode when using the pen, brush or spray for now, lets validate we are using those
            if self.canvas.mode not in ['brush', 'spray', 'pen']:
                msg = QMessageBox()
                msg.setIconPixmap(QPixmap(':/icons/unstable_journey_logo.ico'))
                msg.setText("Symmetry mode unavailable")
                msg.setInformativeText("Symmetry mode works only with Brush, Pen or Spray modes at the moment.")
                msg.setWindowTitle("Info")
                msg.exec()
                self.symmetryButton.toggle()
        self.canvas.symmetryActive = self.symmetryButton.isChecked()

    def showHelp(self):
        msg = QMessageBox()
        msg.setIconPixmap(QPixmap(':/icons/unstable_journey_logo.ico'))
        msg.setText("Help")
        msg.setInformativeText("""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
        p, li { white-space: pre-wrap; }
        hr { height: 1px; border-width: 0; }
        li.unchecked::marker { content: "\2610"; }
        li.checked::marker { content: "\2612"; }
        </style></head><body style=" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;">
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Remember to start <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs"><span style=" text-decoration: underline; color:#094fd1;">automatic1111 webui</span></a> with the <span style=" font-weight:700;">--api </span><a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#webui-user"><span style=" text-decoration: underline; color:#094fd1;">COMMANDLINE_ARGS</span></a> in order to allow this application to work correctly. If the host is not your computer (friend with nice GPU or server), you can also add the <span style=" font-weight:700;">--listen </span>parameter (webui-user.bat or .sh).</p>
        <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Enable HTTPS if using gradio URL (using --share instead of --listen gives you a gradio https URL).        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">If you use ControlNet (CN), there's a bug in latest version, if it's not fixed yet, you will have to switch to a previous commit <span style=" text-decoration: underline;">from the extension folder</span> executing the following commands: <span style=" font-weight:700;">git checkout</span> <span style=" font-family:'Helvetica Neue'; font-weight:700;">c5403ce </span><span style=" font-family:'Helvetica Neue';">(c5403ced564e1042dcf2cf4acdd0967373b14343 hash). </span>        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Helvetica Neue';">Just in case, the latest automatic1111 commit working with this application is 22bcc7 (22bcc7be428c94e9408f589966c2040187245d81).</span>        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">You should also update <span style=" color:#ff2600;">this</span> project using <span style=" font-weight:700;">git pull </span>when updates are rolled out.        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">        </p>
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">If you would like to contribute or ask questions, reach out on <a href="https://discord.gg/9wKuxN7aaq"><span style=" text-decoration: underline; color:#094fd1;">Discord</span></a>        </p></body></html>
        """)
        msg.setWindowTitle("Help")
        msg.exec()


    def cnModelComboBoxChanged(self, model):
        print("cnModelComboBoxChanged")
        self.cnSelectedModel = model

    def cnPreComboBoxChanged(self, module):
        print("cnPreComboBoxChanged")
        self.cnSelectedModule = module

    def modelComboBoxChanged(self, model):
        print("ModelComboBoxChanged")
        self.refreshModelButton.setEnabled(False)
        self.modelComboBox.setEnabled(False)
        
        worker = Worker(self, self.changeModelJob, model)
        worker.signals.result.connect(self.changeModelResultHandler)
        threadpool = QThreadPool.globalInstance()
        threadpool.start(worker)

    def changeModelJob(self, model):
        options = {}
        options['sd_model_checkpoint'] = model
        return self.api.set_options(options)

    def changeModelResultHandler(self, result):
        if result is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Make sure your automatic1111 stable diffusion API is enabled with --api launch arg. See logs for details.')
            msg.setWindowTitle("Error")
            msg.exec()
        self.refreshModelButton.setEnabled(True)
        self.modelComboBox.setEnabled(True)

    def refreshCNModel(self):
        print("RefreshCNModel")
        self.refreshCNModelButton.setEnabled(False)
        self.cnModelComboBox.setEnabled(False)
        self.cnPreComboBox.setEnabled(False)

        worker = Worker(self, self.refreshCNModelJob)
        worker.signals.result.connect(self.refreshCNModelResultHandler)
        threadpool = QThreadPool.globalInstance()
        threadpool.start(worker)

    def refreshCNModelJob(self):
        r = self.api.custom_get('controlnet/module_list')
        r2 = self.api.custom_get('controlnet/model_list')
        res = {}
        res['module_list'] = r['module_list']
        res['model_list'] = r2['model_list']
        return res

    def refreshCNModelResultHandler(self, result):
        print(result)
        if result is not None:
            for module in result['module_list']:
                if self.cnPreComboBox.findText(module) == -1: # is not in the list
                    self.cnPreComboBox.addItem(module, module)
            for model in result['model_list']:
                if self.cnModelComboBox.findText(model) == -1: # is not in the list
                    self.cnModelComboBox.addItem(model, model)
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Make sure your automatic1111 stable diffusion API is enabled with --api launch arg. See logs for details.')
            msg.setWindowTitle("Error")
            msg.exec()

        self.refreshCNModelButton.setEnabled(True)
        self.cnModelComboBox.setEnabled(True)
        self.cnPreComboBox.setEnabled(True)


    def refreshModel(self):
        print("RefreshModel")
        self.refreshModelButton.setEnabled(False)
        self.modelComboBox.setEnabled(False)

        worker = Worker(self, self.refreshModelJob)
        worker.signals.result.connect(self.refreshModelResultHandler)
        threadpool = QThreadPool.globalInstance()
        threadpool.start(worker)

    def refreshModelJob(self):
        self.api.refresh_checkpoints()
        return self.api.get_sd_models()

    def refreshModelResultHandler(self, result):
        if result is not None:
            titles = [d['title'] for d in result]
            for title in titles:
                if self.modelComboBox.findText(title) == -1: # is not in the list
                    self.modelComboBox.addItem(title, title)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Make sure your automatic1111 stable diffusion API is enabled with --api launch arg. See logs for details.')
            msg.setWindowTitle("Error")
            msg.exec()

        self.refreshModelButton.setEnabled(True)
        self.modelComboBox.setEnabled(True)


    def replaceCanvasFromSD(self):
        print("ReplaceCanvasFromSD")

        replaceSDButton = getattr(self, 'replaceSDButton')
        replaceSDButton.setEnabled(False)

        worker = Worker(self, self.replaceCanvasFromSDJob)
        worker.signals.result.connect(self.enableReplaceSDButton)
        threadpool = QThreadPool.globalInstance()
        threadpool.start(worker)
        

    def replaceCanvasFromSDJob(self):
        pixmap = self.sdCanvas.pixmap()
        self.canvas.setPixmap(pixmap)

    def enableReplaceSDButton(self):
        replaceSDButton = getattr(self, 'replaceSDButton')
        replaceSDButton.setEnabled(True)

    def convertCanvasToSD(self):
        print("ConvertCanvasToSD")
        convertSDButton = getattr(self, 'convertSDButton')
        convertSDButton.setEnabled(False)

        worker = Worker(self, self.convertCanvasToSDJob)
        worker.signals.result.connect(self.enableConvertSDButton)
        threadpool = QThreadPool.globalInstance()
        threadpool.start(worker)

    def enableConvertSDButton(self, result):
        if result is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Make sure your automatic1111 stable diffusion API is enabled with --api launch arg. See logs for details.')
            msg.setWindowTitle("Error")
            msg.exec()
        convertSDButton = getattr(self, 'convertSDButton')
        convertSDButton.setEnabled(True)

    def convertCanvasToSDJob(self):

        input_path = expanduser("~") + "/NOT_A_FANTASY/paint/input/1.png" 
        if input_path:
            pixmap = self.canvas.pixmap()
            pixmap.save(input_path, "PNG" )

            # pixmap to pil image
            img = pixmap.toImage() #QImage
            bio = io.BytesIO()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            img.save(buffer, "PNG")
            byte_arr = buffer.data()
            bio.write(byte_arr.data())
            buffer.close()
            bio.seek(0)
            pil_img = Image.open(bio)

            
            #self.cn_unit1 = webuiapi.ControlNetUnit(input_image=pil_img, module='canny', model='control_v11p_sd15_lineart [43d4be0d]')
            #self.cn_unit1 = webuiapi.ControlNetUnit(input_image=pil_img, module='scribble', model='control_v11p_sd15_scribble [d4ba51ff]', guessmode=True)
            #self.cn_unit1 = webuiapi.ControlNetUnit(input_image=pil_img, module='canny', model='control_v11p_sd15_canny [d14c016b]', guessmode=True)
            #self.cn_unit2 = webuiapi.ControlNetUnit(input_image=pil_img, module='canny', model='control_canny-fp16 [e3fe7712]', guessmode=True)
            print(self.cnSelectedModel)
            print(self.cnSelectedModule)
            cn_unit1 = webuiapi.ControlNetUnit(input_image=pil_img, module=self.cnSelectedModule, model=self.cnSelectedModel)
            cn_units = []
            print(self.cnSelectedModule)
            if self.cnSelectedModel is not None:
                cn_units = [cn_unit1]

            # inputs
            if not self.seedLineEdit.text():
                self.randomizeSeed()

            result1 = self.api.img2img(
                images=[pil_img], 
                prompt=str(self.promptTextEdit.toPlainText()),
                negative_prompt=self.negativePromptTextEdit.toPlainText(),
                seed=int(self.seedLineEdit.text()), 
                cfg_scale=float(self.cfgDoubleSpinBox.value()), 
                controlnet_units=cn_units,
                denoising_strength=self.denoisingDoubleSpinBox.value(),
                sampler_name=self.samplerComboBox.currentText(),
                steps=self.stepsSpinBox.value(),
                
                )

            qim = ImageQt(result1.image)
            newPixmap = QPixmap.fromImage(qim)
            self.sdCanvas.setPixmap(newPixmap)
            # save file to disk too, we aren't batch generating after all.
            self.save_dir = expanduser('~') + "/NOT_A_FANTASY/paint/output/"
            if not path.exists(self.save_dir):
                makedirs(self.save_dir)

            metadata = PngInfo()
            metadata.add_text("parameters", str(result1.parameters))
            result1.image.save(f"{self.save_dir}/{time.strftime('%Y%m%d-%H%M%S')}.png", pnginfo=metadata)
            

    def save_file(self):
        """
        Save active canvas to image file.
        :return:
        """
        input_path, _ = QFileDialog.getSaveFileName(self, "Save file", "masterpiece", "PNG Image file (*.png)")

        if input_path:
            pixmap = self.canvas.pixmap()
            pixmap.save(input_path, "PNG" )

    def invert(self):
        img = QImage(self.canvas.pixmap())
        img.invertPixels()
        pixmap = QPixmap()
        pixmap.convertFromImage(img)
        self.canvas.setPixmap(pixmap)

    def flip_horizontal(self):
        pixmap = self.canvas.pixmap()
        self.canvas.setPixmap(pixmap.transformed(QTransform().scale(-1, 1)))

    def flip_vertical(self):
        pixmap = self.canvas.pixmap()
        self.canvas.setPixmap(pixmap.transformed(QTransform().scale(1, -1)))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/unstable_journey_logo.ico'))
    window = MainWindow()
    app.exec()
