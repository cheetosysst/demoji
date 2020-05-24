# demoji
An emoji picker built for tiling window mangers like i3 and bspwm

This project is inspired by [Luke Smith](https://github.com/lukesmithxyz)'s video [dmenu tips: Emojis and more](https://youtu.be/UCEXY46t3OA). If you like this concept, please go and subscribe to the original creator.

## Usage
### Picker
Please download and install dmenufirst. I'm using the one come with [Endeavour OS](https://endeavouros.com/). Start the test after you finish setting up the enviroment.

``` bash
sh demoji.sh
```

Search for the emoji you want and press ENTER. You'll see a notification (in traditional Chinese, since that's hte language I'm using) telling you it's in the clipboard. You can then paste it anywhere you want. Some distro doesn't come with fonts with emoji charactor, then you'll have to change system font or install Cairo. I suggest using the latter one, because changing the font might break the overall aesthetic of the distro.

If it all works well, you can now start installing it to your system. If you're using i3 or i3-gaps, you can simply add the following command to your config file. NOTICE, demoji.sh has to be in the same directory as the emoji_list, so the scrpit knows where to look for it's data.

``` bash
bindsym $mod+e exec "sh /path/to/your/demoji.sh"
```

You can change "$mod+e" to any shortcut key combination you prefer. For i3 syntax and usage, please read [i3 User’s Guide](https://i3wm.org/docs/userguide.html#configuring). After resetting i3 config, if no error occur, means you can call the picker by pressing Mod+E (NOTE: Mod key is usually assign to Super key, or as many people calls it, "Windows key").

It should be pretty much the same in bspwm, please test it yourself if using bspwm or other DE.

### List Generator
Please download Python3 first, and install bs4 and requests with pip.

``` bash
pip install bs4 requests
```

If the unicode standard adds new emoji, and wikipedia updates the changes, run this command to get new emojis.

``` bash
python process.py
# Because python2 isn't maintained anymore, here we assume you're using python3 and understands the differance between these two.
```

Check the emoji_list to see if the contents are correct.

### Data format
Inside emoji_list, the data format is

```
<Emoji> <Unicode> <Name>
```
