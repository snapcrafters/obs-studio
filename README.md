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

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/obs-studio)

# Batteries included

The snap of OBS studio comes pre-loaded with some additions features and plugins.

  * FFmpeg supports **nvenc and VA-API accelerated video encoding**.
  * **[Browser](https://github.com/obsproject/obs-browser)** plugin; add web sources to your stream.
  * **[Websockets](https://github.com/Palakis/obs-websocket)** plugin; compatible with [StreamControl](https://play.google.com/store/apps/details?id=dev.t4ils.obs_remote&hl=en) and other remote controls.
```
sudo apt install v4l2loopback-utils v4l2loopback-dkms
sudo modprobe v4l2loopback video_nr=99 card_label="OBS VitualCam" exclusive_caps=1
```
  * **[Advanced Scene Switcher](https://github.com/WarmUpTill/SceneSwitcher)** plugin.
  * **[Source Switcher](https://github.com/exeldro/obs-source-switcher)** plugin.
  * **[Move Transition](https://github.com/exeldro/obs-move-transition)** plugin.