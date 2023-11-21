
# Unstable Journey (codename Icnivad)

A desktop Paint application, with basic Tablet support, powered by Stable Diffusion, automatic1111 webui and PieCasso!

<img alt="Unstable Journey Logo" src="unstable_journey_logo.png" width=100px height=100px >

Express yourself with Unstable Journey, the only drawing application to feature
ready to make pictures of pie, with AI!

<img alt="Unstable Journey" src="showcase.png" width=50% height=50%>

## Dependencies

First, you need to have [AUTOMATIC1111 webui installed and running](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs).

Second, you need to modify webui-user.bat (Windows) or .sh (Linux) in the AUTOMATIC1111 webui install folder to add the **--api** [COMMANDLINE_ARGS, as explained here](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#webui-user). Optional: You can also add the **--listen** argument if you'll connect to another computer/server hosting the webui instad of using localhost:7860

Third, you need to have **git** and **python 3** installed (haven't tested other versions).

And Lastly, AUTOMATIC1111 webui is evolving every day and this application was tested against a specific version, so you might need to do `git checkout 22bcc7` in order for this to work.

## Install

```
git clone https://github.com/rulyone/unstable_journey.git
cd unstable_journey
pip3 install -r requirements.txt
```

If everything is success, you should be able to run it:

```
python3 unstable_journey.py
```

## Troubleshooting and Questions

This is a Python Desktop application written to work with AUTO1111 webui as a backend.

Remember to start automatic1111 webui with the --api COMMANDLINE_ARGS in order to allow this application to work correctly. If the host is not your computer (friend with nice GPU or server), you can also add the --listen parameter (webui-user.bat or .sh).

If you use ControlNet (CN), there's a bug in latest version, if it's not fixed yet, you will have to switch to a previous commit from the extension folder executing the following commands: git checkout c5403ce (c5403ced564e1042dcf2cf4acdd0967373b14343 hash).

Just in case, the latest automatic1111 commit working with this application is 22bcc7, so you might need to do a `git checkout 22bcc7` (22bcc7be428c94e9408f589966c2040187245d81).

Join the Discord server if you would like to contribute or have any questions

https://discord.gg/9wKuxN7aaq