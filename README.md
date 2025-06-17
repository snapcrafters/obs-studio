<h1 align="center">
  <img src="https://avatars1.githubusercontent.com/u/7725691?v=3&s=256" alt="OBS Studio">
  <br />
  OBS Studio
</h1>

<p align="center"><b>This is the snap of <a href="https://obsproject.com/" target=_blank">OBS Studio</a></b></p>
<p align="center">
<a href="https://snapcraft.io/obs-studio"><img alt="Snap Badge" src="https://snapcraft.io/obs-studio/badge.svg" /></a>
<a href="https://snapcraft.io/obs-studio"><img alt="Snap Installs" src="https://img.shields.io/badge/Installs-89.1k-2E7725?logo=snapcraft"></a>
<a href="https://github.com/snapcrafters/obs-studio/actions/workflows/sync-upstream.yml"><img src="https://github.com/snapcrafters/obs-studio/actions/workflows/sync-upstream.yml/badge.svg"></a>
<a href="https://github.com/snapcrafters/obs-studio/actions/workflows/release-to-candidate.yml"><img src="https://github.com/snapcrafters/obs-studio/actions/workflows/release-to-candidate.yml/badge.svg"></a>
<a href="https://github.com/snapcrafters/obs-studio/actions/workflows/promote-to-stable.yml"><img src="https://github.com/snapcrafters/obs-studio/actions/workflows/promote-to-stable.yml/badge.svg"></a>
</p>

<!-- Uncomment and modify this when you have a screenshot
![my-snap-name](screenshot.png?raw=true "my-snap-name")
-->

<p align="center">Published for <img src="https://raw.githubusercontent.com/anythingcodes/slack-emoji-for-techies/gh-pages/emoji/tux.png" align="top" width="24" /> with 💝 by Snapcrafters</p>

## Install

```shell
sudo snap install obs-studio
sudo snap connect obs-studio:avahi-control
sudo snap connect obs-studio:kernel-module-observe
sudo snap connect obs-studio:screencast-legacy
```

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/obs-studio)

## Wayland

Screen and Window capture in a Wayland session is supported in OBS 27.0.0 or
newer.

## Removable Storage

To access content on external storage, manually connect to the removable-media plug:

```shell
snap connect obs-studio:removable-media
```

## Camera

To access camera, manually connect to the camera plug:

```shell
snap connect obs-studio:camera
```

## OBS Virtual Camera

Starting with OBS Studio 26.1, Virtual Camera support is integrated. The
`Start Virtual Camera` button is located in the Controls pane, just below
`Start Recording`.

Here's how to install and configure `v4l2loopback` which OBS uses:

```shell
sudo snap connect obs-studio:kernel-module-observe
sudo apt -y install v4l2loopback-dkms v4l2loopback-utils
echo 'options v4l2loopback devices=1 video_nr=13 card_label="OBS Virtual Camera" exclusive_caps=1' | sudo tee /etc/modprobe.d/v4l2loopback.conf
echo "v4l2loopback" | sudo tee /etc/modules-load.d/v4l2loopback.conf
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=13 card_label="OBS Virtual Camera" exclusive_caps=1
```

**NOTE!** Using `video_nr` greater than 64 will not work.

## NDI

If you want to use the [NDI](https://github.com/Palakis/obs-ndi) plugin you'll need to connect the Avahi Control interface.

```shell
snap connect obs-studio:avahi-control
```

## Browser

Optional interfaces can be connected that integrate with Browser Sources and Custom Browser Socks.

### Process Control

The OBS Browser does attempt to adjust the scheduler priority, you can enable this capability by optionally connecting the `process-control` interface.

```shell
snap connect obs-studio:process-control
```

### Passwords and Keys

The browser in OBS can obtain user credentials from applications such as GNOME Passwords and Keys (seahorse) or Kwallet, should you want it to.

```shell
snap connect obs-studio:password-manager-service
```
