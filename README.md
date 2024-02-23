<h1 align="center">
  <img src="https://avatars1.githubusercontent.com/u/7725691?v=3&s=256" alt="OBS Studio">
  <br />
  OBS Studio
</h1>

<p align="center"><b>This is the snap of <a href="https://obsproject.com/" target=_blank">OBS Studio</a></b>, pre-loaded with extra features and a curated collection of 3rd party OBS Studio plugins for live streaming and screen recording.</p>
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

# Batteries included

The OBS Studio snap is built from [wimpysworld/obs-studio-portable](https://github.com/wimpysworld/obs-studio-portable). Additionally, the OBS Studio snap includes the following features:

- Includes **50 of the best 3rd Party plugins for OBS Studio**!
- Chromium Embedded Frameworks (CEF) to enable Browser Sources
- NVENC (NVIDIA) and VA-API (AMD & Intel) accelerated video encoding
- Shader and GStreamer effects filters
- Fraunhofer FDK AAC Codec
- Pipewire application specific audio capture
- VLC and GStreamer Media sources
- AJA NTV2 SDK
- [WebSockets](https://github.com/obsproject/obs-websocket) 5.x and 4.9.1-compat are both included
- [NewTek NDI™ integration](https://github.com/obs-ndi/obs-ndi) and [Teleport](https://github.com/fzwoch/obs-teleport) support
- [SRT & RIST Protocol](https://obsproject.com/wiki/Streaming-With-SRT-Or-RIST-Protocols) support
- Markdown, Pango and API text sources

## OBS Studio Plugins

Thanks to the OBS Studio developers and developers of the growing list of excellent plugins.
OBS Studio Portable for Linux celebrates the best of what's available. Thank you! 🙇

Here are the 3rd party plugins that come bundled with the OBS Studio snap:

### Audio 🔉

- **[Audio Pan](https://github.com/norihiro/obs-audio-pan-filter)** plugin; control stereo pan of audio sources.
- **[Local Vocal](https://github.com/obs-ai/obs-localvocal)** plugin; local speech and text AI processing routines and AI transcription.
- **[Mute Filter](https://github.com/norihiro/obs-mute-filter)** plugin; to mute audio from a source.
- **[PipeWire Audio Capture](https://github.com/dimtpap/obs-pipewire-audio-capture)** plugin; capture application audio from PipeWire.
- **[Scale to Sound](https://github.com/Qufyy/obs-scale-to-sound)** plugin; adds a filter which makes a source scale based on the audio levels of any audio source you choose
- **[Soundboard](https://github.com/cg2121/obs-soundboard)** plugin; adds a soundboard dock.
- **[Waveform](https://github.com/phandasm/waveform)** plugin; audio spectral analysis.

### Automation 🎛

- **[Advanced Scene Switcher](https://github.com/WarmUpTill/SceneSwitcher)** plugin; an automated scene switcher.
- **[Directory Watch Media](https://github.com/exeldro/obs-dir-watch-media)** plugin; filter you can add to a media source to load the oldest or newest file in a directory.
- **[Dummy Source](https://github.com/norihiro/obs-command-source)** plugin; provides a dummy source to execute arbitrary commands when a scene is switched.
- **[Source Switcher](https://github.com/exeldro/obs-source-switcher)** plugin; to switch between a list of sources.
- **[Transition Table](https://github.com/exeldro/obs-transition-table)** plugin; customize scene transitions.
- **[Websockets](https://github.com/obsproject/obs-websocket)** plugin; remote-control OBS Studio through WebSockets.
  - 5.x and 4.9.1-compat are both included

### Effects ✨

- **[3D Effect](https://github.com/exeldro/obs-3d-effect)** plugin; 3D effect filter.
- **[Browser Transition](https://github.com/exeldro/obs-browser-transition)** plugin; show a browser source during scene transition.
- **[Composite Blur](https://github.com/FiniteSingularity/obs-composite-blur)** plugin; comprehensive blur plugin that provides several different blur algorithms, and proper compositing.
- **[DVD Screensaver](https://github.com/univrsal/dvds3)** plugin; a DVD screen saver source type.
- **[Downstream Keyer](https://github.com/exeldro/obs-downstream-keyer)** plugin; add a Downstream Keyer dock.
- **[Dynamic Delay](https://github.com/exeldro/obs-dynamic-delay)** plugin; filter for dynamic delaying a video source.
- **[Face Tracker](https://github.com/norihiro/obs-face-tracker)** plugin; face tracking plugin
- **[Freeze Filter](https://github.com/exeldro/obs-freeze-filter)** plugin; freeze a source using a filter.
- **[Gradient](https://github.com/exeldro/obs-gradient-source)** plugin; adding gradients as a source.
- **[Move Transition](https://github.com/exeldro/obs-move-transition)** plugin; move source to a new position during a scene transition.
- **[Multi Source Effect](https://github.com/norihiro/obs-multisource-effect)** plugin; provides a custom effect to render multiple sources.
- **[Pixel Art](https://github.com/dspstanky/pixel-art)** plugin; create retro-inspired pixel art visuals.
- **[Recursion Effect](https://github.com/exeldro/obs-recursion-effect)** plugin; recursion effect filter.
- **[Replay Source](https://github.com/exeldro/obs-replay-source)** plugin; slow motion replay async sources from memory.
- **[RGB Levels](https://github.com/wimpysworld/obs-rgb-levels-filter)** plugin; simple filter to adjust RGB levels.
- **[Scene as Transition](https://github.com/andilippi/obs-scene-as-transition)** plugin; use scenes as transitions.
- **[Shader Filter](https://github.com/exeldro/obs-shaderfilter)** plugin; for applying an arbitrary shader to a source.
- **[Stroke Glow Shadow](https://github.com/FiniteSingularity/obs-stroke-glow-shadow)** plugin; provide efficient Stroke, Glow, and Shadow effects on masked sources.
- **[Time Shift](https://github.com/exeldro/obs-time-shift)** plugin; time shift a source using a filter.
- **[Time Warp Scan](https://github.com/exeldro/obs-time-warp-scan)** plugin; a time warp scan filter.
- **[Vintage Filter](https://github.com/cg2121/obs-vintage-filter)** plugin; a filter to make source black & white or sepia.

### Encoding & Output 🎞

- **[Game Capture](https://github.com/nowrep/obs-vkcapture)** plugin; Vulkan/OpenGL game capture.
- **[GStreamer](https://github.com/fzwoch/obs-gstreamer)** plugin; feed GStreamer launch pipelines into OBS Studio.
- **[NDI](https://github.com/obs-ndi/obs-ndi)** plugin; Network A/V in OBS Studio with NewTek's NDI technology.
- **[Source Record](https://github.com/exeldro/obs-source-record)** plugin; make sources available to record via a filter.
- **[StreamFX](https://github.com/Xaymar/obs-StreamFX)** plugin; unlocks the full potential of NVENC along with encoders for Avid DNxHR, Apple ProRes and CineForm.
  - **Only the _stable_ StreamFX encoders, Color Grading and Dynamic Mask filters are enabled in OBS Studio Portable for Linux**.
- **[Teleport](https://github.com/fzwoch/obs-teleport)** plugin; open NDI-like replacement. (_not NDI compatible_)
- **[VA-API](https://github.com/exeldro/obs-transition-table)** plugin; GStreamer-based VA-API encoder implementation.
- **[Vertical Canvas](https://github.com/Aitum/obs-vertical-canvas)** plugin; make content for TikTok, YouTube Shorts, Instagram Live, and more without the fuss.

### Tools 🛠

- **[Scene Notes Dock](https://github.com/exeldro/obs-scene-notes-dock)** plugin; create a Dock for showing and editing notes for the currently active scene.
- **[Source Clone](https://github.com/exeldro/obs-source-clone)** plugin; add source cloning
- **[Source Copy](https://github.com/exeldro/obs-source-copy)** plugin; adds copy-and-paste options to the tools menu.
- **[Source Dock](https://github.com/exeldro/obs-source-dock)** plugin; adds browser sources as custom docks.

### Text 📝

- **[Markdown](https://github.com/exeldro/obs-markdown)** plugin; add Markdown sources
- **[Text PThread](https://github.com/norihiro/obs-text-pthread)** plugin; Rich text source plugin with many advanced features, including multi-language support, emoji support, vertical rendering and RTL support.
- **[URL Source](https://github.com/obs-ai/obs-urlsource)** plugin; fetch data from a URL (API), parse and display live update in scene.

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

The OBS Studio snap bundles `libgamepad`, `libuihook` and `netlib` so that if
you want to use the [Input Overlay](https://github.com/univrsal/input-overlay)
plugin, you can install it as outlined above then connect the joystick
interface as follows.

```shell
snap connect obs-studio:joystick
```

_The Input Overlay plugin is not shipped by default in the OBS Studio snap
because it introduced excessive CPU utilisation when bundled, although
works fine as a user-installed plugin. So we've made it as easy as possible
to add it yourself should you need it._

## Wayland

Screen and Window capture in a Wayland session is supported in OBS 27.0.0 or
newer.

## Removable Storage

To access content on external storage, manually connect to the removable-media plug:

```shell
snap connect obs-studio:removable-media
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
