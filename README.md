<h1 align="center">
  <img src="https://avatars1.githubusercontent.com/u/7725691?v=3&s=256" alt="OBS Studio">
  <br />
  OBS Studio
</h1>

<p align="center"><b>This is the snap for OBS Studio</b>, <i>“Free and open source software for live streaming and screen recording; the snap comes pre-loaded with extra features and plugins!”</i> It works on Ubuntu, Fedora, Debian, and other major Linux distributions.</p>

<p align="center">
<a href="https://build.snapcraft.io/user/snapcrafters/obs-studio"><img src="https://build.snapcraft.io/badge/snapcrafters/obs-studio.svg" alt="Snap Status"></a>
</p>

<!-- Uncomment and modify this when you have a screenshot
![my-snap-name](screenshot.png?raw=true "my-snap-name")
-->

<p align="center">Published for <img src="https://raw.githubusercontent.com/anythingcodes/slack-emoji-for-techies/gh-pages/emoji/tux.png" align="top" width="24" /> with 💝 by Snapcrafters</p>

## Install

    sudo snap install obs-studio
    sudo snap connect obs-studio:audio-record
    sudo snap connect obs-studio:camera
    sudo snap connect obs-studio:jack1
    sudo snap connect obs-studio:joystick
    sudo snap connect obs-studio:removable-media

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/obs-studio)

# Batteries included

The snap of OBS studio comes pre-loaded with some additions features and plugins.

  * FFmpeg supports **nvenc (NVIDIA) and VA-API (AMD & Intel) accelerated video encoding**.
  * **[Advanced Scene Switcher](https://github.com/WarmUpTill/SceneSwitcher)** plugin; an automated scene switcher.
  * **[Browser](https://github.com/obsproject/obs-browser)** plugin; CEF-based OBS Studio browser plugin.
  * **[DVD Screensaver](https://github.com/univrsal/dvds3)** plugin; a DVD screen saver source type.
  * **[Freeze Filter](https://github.com/exeldro/obs-freeze-filter)** plugin; freeze a source using a filter.
  * **[Input Overlay](https://github.com/univrsal/input-overlay)** plugin; show keyboard, gamepad and mouse input on stream.
  * **[Move Transition](https://github.com/exeldro/obs-move-transition)** plugin; move source to a new position during scene transition.
  * **[NDI](https://github.com/Palakis/obs-ndi)** plugin; Network A/V via NewTek's NDI.
  * **[Replay Source](https://github.com/exeldro/obs-replay-source)** plugin; slow motion replay async sources from memory.
  * **[Scrab](https://github.com/univrsal/scrab)** plugin; adds a configurable hotkey to quickly select a screen region and add it as an image source to the current scene.
  * **[Source Switcher](https://github.com/exeldro/obs-source-switcher)** plugin; to switch between a list of sources.
  * **[Spectralizer](https://github.com/univrsal/spectralizer)** plugin; audio visualization using fftw.
  * **[StreamFX](https://github.com/Xaymar/obs-StreamFX)** plugin; collection modern effects filters and transitions.
  * **[Transition Matrix](https://github.com/admshao/obs-transition-matrix)** plugin; customize Any -> One or One -> One scene transitions.
  * **[V4L2Sink](https://github.com/CatxFish/obs-v4l2sink)** plugin; provides output capabilities to a Video4Linux2 device to create virtual webcams.
  * **[Vintage Filter](https://github.com/cg2121/obs-vintage-filter)** plugin; black & white or sepia source filter.
  * **[Websockets](https://github.com/Palakis/obs-websocket)** plugin; remote-control OBS Studio through WebSockets, compatible with [StreamControl](https://play.google.com/store/apps/details?id=dev.t4ils.obs_remote&hl=en).

## V4L2Sink

To make use of the V4L2Sink plugin to create a virtual webcam, install
and configure `v4l2loopback` as follows:

```
sudo apt -y install v4l2loopback-dkms v4l2loopback-utils
echo "options v4l2loopback devices=1 video_nr=99 card_label=VirtualCam exclusive_caps=1" | sudo tee /etc/modprobe.d/v4l2loopback.conf
echo "v4l2loopback" | sudo tee /etc/modules-load.d/v4l2loopback.conf
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=99 card_label=VirtualCam exclusive_caps=1"
```

Then use `/dev/video99` as the path to V4L2 device in *Tools -> V4L2 Video Output*.

## Input Overlay

If you want to use the Input Overlay plugin you will need to connect the Joystick interface.

```
snap connect obs-studio:joystick
```