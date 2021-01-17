<h1 align="center">
  <img src="https://avatars1.githubusercontent.com/u/7725691?v=3&s=256" alt="OBS Studio">
  <br />
  OBS Studio
</h1>

<p align="center"><b>This is the snap for OBS Studio</b>, <i>“Free and open source software for live streaming and screen recording; the snap comes pre-loaded with extra features and plugins!”</i> It works on Ubuntu, Fedora, Debian, and other major Linux distributions.</p>

<p align="center">
<a href="https://snapcraft.io/obs-studio"><img alt="obs-studio" src="https://snapcraft.io/obs-studio/badge.svg" /></a>
<a href="https://snapcraft.io/obs-studio"><img alt="obs-studio" src="https://snapcraft.io/obs-studio/trending.svg?name=0" /></a>
</p>

<!-- Uncomment and modify this when you have a screenshot
![my-snap-name](screenshot.png?raw=true "my-snap-name")
-->

<p align="center">Published for <img src="https://raw.githubusercontent.com/anythingcodes/slack-emoji-for-techies/gh-pages/emoji/tux.png" align="top" width="24" /> with 💝 by Snapcrafters</p>

## Install

    sudo snap install obs-studio
    sudo snap connect obs-studio:audio-record
    sudo snap connect obs-studio:avahi-control
    sudo snap connect obs-studio:camera
    sudo snap connect obs-studio:kernel-module-observe

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/obs-studio)

# Batteries included

The snap of OBS studio comes pre-loaded with some additional features and plugins.

  * Supports **nvenc (NVIDIA) and VA-API (AMD & Intel) accelerated video encoding**.
  * **[Advanced Scene Switcher](https://github.com/WarmUpTill/SceneSwitcher)** plugin; an automated scene switcher.
  * **[Audio Pan](https://github.com/norihiro/obs-audio-pan-filter)** plugin; control stereo pan of audio source.
  * **[Browser](https://github.com/obsproject/obs-browser)** plugin; CEF-based OBS Studio browser plugin.
  * **[Directory Watch Media](https://github.com/exeldro/obs-dir-watch-media)** plugin; filter you can add to media source to load the oldest or newest file in a directory.
  * **[DVD Screensaver](https://github.com/univrsal/dvds3)** plugin; a DVD screen saver source type.
  * **[Dynamic Delay](https://github.com/exeldro/obs-dynamic-delay)** plugin; filter for dynamic delaying a video source.
  * **[Freeze Filter](https://github.com/exeldro/obs-freeze-filter)** plugin; freeze a source using a filter.
  * **[gPhoto](https://github.com/adlerweb/obs-gphoto)** plugin; connect DSLR cameras with obs-studio via gPhoto.
  * **[Gradient Source](https://github.com/exeldro/obs-gradient-source)** plugin; adding gradients as a Soource.
  * **[GStreamer](https://github.com/fzwoch/obs-gstreamer)** plugins; feed GStreamer launch pipelines into OBS Studio and use GStreamer encoder elements.
  * **[Move Transition](https://github.com/exeldro/obs-move-transition)** plugin; move source to a new position during scene transition.
  * **[NDI](https://github.com/Palakis/obs-ndi)** plugin; Network A/V via NewTek's NDI.
  * **[Recursion Effect](https://github.com/exeldro/obs-recursion-effect)** plugin; recursion effect filter.
  * **[Replay Source](https://github.com/exeldro/obs-replay-source)** plugin; slow motion replay async sources from memory.
  * **[RGB Levels](https://github.com/petrifiedpenguin/obs-rgb-levels-filter)** plugin; simple filter to adjust RGB levels.
  * **[RTSPServer](https://github.com/iamscottxu/obs-rtspserver/)** plugin; encode and publish to a RTSP stream.
  * **[Source Switcher](https://github.com/exeldro/obs-source-switcher)** plugin; to switch between a list of sources.
  * **[Spectralizer](https://github.com/univrsal/spectralizer)** plugin; audio visualization using fftw.
  * **[StreamFX](https://github.com/Xaymar/obs-StreamFX)** plugin; collection modern effects filters and transitions.
  * **[Text Pango](https://github.com/kkartaltepe/obs-text-pango)** plugin; Provides a text source rendered using Pango with multi-language support, emoji support, vertical rendering and RTL support.
  * **[Time Warp Scan](https://github.com/exeldro/obs-time-warp-scan)** plugin; a time warp scan filter.
  * **[Transition Table](https://github.com/exeldro/obs-transition-table)** plugin; customize scene transitions.
  * **[VNC Source](https://github.com/norihiro/obs-vnc)** plugin; VNC viewer that works as a source.
  * **[Websockets](https://github.com/Palakis/obs-websocket)** plugin; remote-control OBS Studio through WebSockets, compatible with [StreamControl](https://play.google.com/store/apps/details?id=dev.t4ils.obs_remote&hl=en).

## Removable Storage

To access content on external storage, manually connect to the removable-media plug:

```
snap connect obs-studio:removable-media
```

## OBS Virtual Camera

Starting with OBS Studio 26.1, Virtual Camera support is integrated. The
`Start Virtual Camera` button is located in the Controls pane, just below
`Start Recording`.

Here's how to install and configure `v4l2loopback` which OBS uses:

```
sudo snap connect obs-studio:kernel-module-observe
sudo apt -y install v4l2loopback-dkms v4l2loopback-utils
echo "options v4l2loopback devices=1 video_nr=13 card_label='OBS Virtual Camera' exclusive_caps=1" | sudo tee /etc/modprobe.d/v4l2loopback.conf
echo "v4l2loopback" | sudo tee /etc/modules-load.d/v4l2loopback.conf
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=13 card_label='OBS Virtual Camera' exclusive_caps=1
```

**NOTE!** Using `video_nr` greater than 64 will not work.

## NDI

If you want to use the [NDI](https://github.com/Palakis/obs-ndi) plugin you'll
need to connect the Avahi Control interface.

```
snap connect obs-studio:avahi-control
```

## Browser

Optional interfaces can be connected that integrate with Browser Sources and Custom Browser Socks.

### Process Control

The OBS Browser does attempt to adjust the scheduler priority, you can enable this capability by optionally connecting the `process-control` interface.

```
snap connect obs-studio:process-control
```

### Passwords and Keys

The browser in OBS can obtain user credentials from applications such as GNOME Passwords and Keys (seahorse) or Kwallet, should you want it to.

```
snap connect obs-studio:password-manager-service
```

## gPhoto

The [gPhoto](https://github.com/adlerweb/obs-gphoto) plugin is bundled and
allows DSLR cameras (mostly Canon) to be connected with obs-studio via USB.
You will need to connect the Raw USB interface.

```
snap connect obs-studio:raw-usb
```

## ALSA & Jack audio

If you use ALSA or Jack audio the you can enable interfaces to those audio systems.

    sudo snap connect obs-studio:alsa
    sudo snap connect obs-studio:jack1

## 3rd Party plugins

You might find that this modified snap of OBS Studio doesn't include a plugin that you use.
To install pre-compiled plugins, download and extract the plugin and put it in
`~/snap/obs-studio/current/.config/obs-studio/plugins/`.

For example, this is how the [Input Overlay](https://github.com/univrsal/input-overlay)
plugin looks when correctly installed:

```
/home/username/snap/obs-studio/current/.config/obs-studio/plugins/
└── input-overlay
    ├── bin
    │   └── 64bit
    │       └── input-overlay.so
    └── data
        └── locale
            ├── de-DE.ini
            ├── en-US.ini
            └── ru-RU.ini
```

### Input Overlay

This snap of OBS Studio comes with `libuihook` and `netlib` pre-installed so
that if you want to use the [Input Overlay](https://github.com/univrsal/input-overlay)
plugin, you can install it as outlined above then connect the joystick
interface as follows.

```
snap connect obs-studio:joystick
```

*The Input Overlay plugin is not shipped by default in the OBS Studio snap
because it introduced excessive CPU utilisation when bundled, although
works fine as a user-installed plugin. So we've made it as easy as possible
to add it yourself should you need it.*

### DroidCam OBS

If you want to use [DroidCam OBS](https://play.google.com/store/apps/details?id=com.dev47apps.obsdroidcam)
you will need to install the accompanying plugin.

  * Download the [DroidCam OBS Plugin for Linux](http://dev47apps.com/obs/)
  * Extract the `droidcam_obs_1.1.1_linux.zip` archive.
  * Put the plugin in `~/snap/obs-studio/current/.config/obs-studio/plugins/`.

```
mv droidcam-obs ~/snap/obs-studio/current/.config/obs-studio/plugins/
```

This is how the DroidCam OBS plugin looks when correctly installed:

```
/home/username/snap/obs-studio/current/.config/obs-studio/plugins/
└── droidcam-obs
    ├── bin
    │   └── 64bit
    │       └── droidcam-obs.so
    └── data
        └── locale
            └── en-US.ini
```
