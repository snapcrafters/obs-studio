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
    sudo snap connect obs-studio:avahi-control
    sudo snap connect obs-studio:camera
    sudo snap connect obs-studio:jack1
    sudo snap connect obs-studio:joystick
    sudo snap connect obs-studio:kernel-module-observe
    sudo snap connect obs-studio:removable-media

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
  * **[GStreamer](https://github.com/fzwoch/obs-gstreamer)** plugins; feed GStreamer launch pipelines into OBS Studio and use GStreamer encoder elements.
  * **[Move Transition](https://github.com/exeldro/obs-move-transition)** plugin; move source to a new position during scene transition.
  * **[NDI](https://github.com/Palakis/obs-ndi)** plugin; Network A/V via NewTek's NDI.
  * **[Replay Source](https://github.com/exeldro/obs-replay-source)** plugin; slow motion replay async sources from memory.
  * **[Recursion Effect](https://github.com/exeldro/obs-recursion-effect)** plugin; add recursion effect to a source using a filter.
  * **[RGB Levels](https://github.com/petrifiedpenguin/obs-rgb-levels-filter)** plugin; simple filter to adjust RGB levels.
  * **[RTSPServer](https://github.com/iamscottxu/obs-rtspserver/)** plugin; encode and publish to a RTSP stream.
  * **[Source Switcher](https://github.com/exeldro/obs-source-switcher)** plugin; to switch between a list of sources.
  * **[Spectralizer](https://github.com/univrsal/spectralizer)** plugin; audio visualization using fftw.
  * **[StreamFX](https://github.com/Xaymar/obs-StreamFX)** plugin; collection modern effects filters and transitions.
  * **[Text Pango](https://github.com/kkartaltepe/obs-text-pango)** plugin; Provides a text source rendered using Pango with multi-language support, emoji support, vertical rendering and RTL support.
  * **[Transition Matrix](https://github.com/admshao/obs-transition-matrix)** plugin; customize Any -> One or One -> One scene transitions.
  * **[V4L2Sink](https://github.com/CatxFish/obs-v4l2sink)** plugin; provides output capabilities to a Video4Linux2 device to create virtual webcams.
  * **[Vintage Filter](https://github.com/cg2121/obs-vintage-filter)** plugin; black & white or sepia source filter.
  * **[VNC Source](https://github.com/norihiro/obs-vnc)** plugin; VNC viewer that works as a source.
  * **[Websockets](https://github.com/Palakis/obs-websocket)** plugin; remote-control OBS Studio through WebSockets, compatible with [StreamControl](https://play.google.com/store/apps/details?id=dev.t4ils.obs_remote&hl=en).

## Removable Storage

To access content on external storage, manually connect to the removable-media plug:

```
snap connect obs-studio:removable-media
```

## V4L2Sink

Connect to the kernel-module-observe plug so that OBS can observer the status of kernel modules:

```
sudo snap connect obs-studio:kernel-module-observe
```

To make use of the V4L2Sink plugin to create a virtual webcam, install
and configure `v4l2loopback` as follows:

```
sudo apt -y install v4l2loopback-dkms v4l2loopback-utils
echo "options v4l2loopback devices=1 video_nr=99 card_label=VirtualCam exclusive_caps=1" | sudo tee /etc/modprobe.d/v4l2loopback.conf
echo "v4l2loopback" | sudo tee /etc/modules-load.d/v4l2loopback.conf
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=99 card_label=VirtualCam exclusive_caps=1
```

Then use `/dev/video99` as the path to V4L2 device in *Tools -> V4L2 Video Output*.

## NDI

If you want to use the [NDI](https://github.com/Palakis/obs-ndi) plugin you'll
need to connect the Avahi Control interface.

```
snap connect obs-studio:avahi-control
```

## gPhoto

The [gPhoto](https://github.com/adlerweb/obs-gphoto) plugin is bundled and
allows DSLR cameras (mostly Canon) to be connected with obs-studio via USB.
You will need to connect the Raw USB interface.

```
snap connect obs-studio:raw-usb
```

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
