# Google Street View Scrape/ Analysis

This python and JS script were copied from different places in the internet that I'm too lazy to reference to... 🤷‍♂️
anyways there's two parts, python script `streetview_v2.py` is your main script you're gonna use to scrape google street view and save it to it's coresponding file. Whilst `mergeScript.js` is there to photomerge bunch of panoramas.

# Setup

To set this up. First you need to setup a virtual environment for python.

```
python3 -m venv .env
```
After which copy this repository to that folder with git or github desktop. luckily there isn't any dependency to install. 

The next step is crucial if you don't want your ip to be banned by google. You first need to create a developer account with google and create a "Street View Static" project. Great thing is you get free credit which is more than enough if you're going to use the scraped data for analysis.

Once your google dev account is created, copy the secret key to a separate file called `key.py`. So the inside of it looks like this.

```
api_key = "pAP4B3z05n15W4tchIngY0u"
```

After setting up the file, you can run it with this command.

```
python3 streetview_v2.py
```
It should start scraping the locations.

once that is done copy the scraped folders into a single folder. Then go to Photoshop File > Scripts > Browse > mergeScript.js

# Editing python for your locations

`streetview_v2.py` was made to scrape the George Street in Sydney for skyview analysis. If you want to apply it to a specific street. You will need coordinates location as well as the distance between the two coordinates. In `location.py`, copy the coordinates and distance into `coor2` and `dist` lists.

```
coor2 = [
    [-33.8795427,151.2052461], # Coordinate 1
    [-33.8743232,151.2067895], # Coordinate 2
    [-33.86870221443746, 151.2069698691709], # Coordinate 3
    [-33.86259456606607, 151.20752876231285] # # Coordinate 4
]

dist = [
    600, # distance between coordinate 1 and 2
    475, # distance between coordinate 2 and 3
    680, # distance between coordinate 3 and 4
]
```

# Editing JS for Photoshop

There are a few things you need to know with this JS Script. First you need to change line 2 for your corresponding photoshop version. 

```
//@includepath "/C/Program Files/Adobe/Adobe Photoshop 2022/Presets/Scripts/"
```
Assuming your Photoshop did not have a custom install, just make sure `Adobe Photoshop 2022` bit of the script is correct to your version of PS.

This script is pretty versitile, although the python script above produces `jpg` images, you can use this JS script for other projects too. Incase those projects uses images like `png`, you can change that settings in line 26.

```
var fList = folders[i].getFiles('*.jpg');
```
just change `'*.jpg'` to `'*.png'` if the tiled images are different file format.

Another Set of setting you can play around with are from lines 28 to 39.
```
// override Photomerge.jsx settings. Default is "Auto". Uncomment to override the default.
photomerge.alignmentKey = "Auto";
//photomerge.alignmentKey   = "Prsp";
//photomerge.alignmentKey   = "cylindrical";
//photomerge.alignmentKey   = "spherical";
//photomerge.alignmentKey   = "sceneCollage";
//photomerge.alignmentKey = "translation"; // "Reposition" in layout dialog   

// other setting that may need to be changed. Defaults below
photomerge.advancedBlending = false; // 'Blend Images Together' checkbox in dialog
photomerge.lensCorrection = false; // Geometric Distortion Correction'checkbox in dialog
photomerge.removeVignette = false; // 'Vignette Removal' checkbox in dialog
```
These all correspondes to the Automate Photo Merge Window that pops out when you select it. lines 28 to 34 are about the layout whilst 36 to 39 are additional setting. There's is no content aware fill though... not sure what the object name is for that.

![Photoshop Photo Merge](https://github.com/JackD-FP/streetview_scrape/blob/main/Screenshot%202022-04-29%20091709.png)

Finally for lines 58 to 63, these lines corresponds to what kind of files are outputed by the script. at the moment it Saves a jpg and psd in the child folder and another jpg in the parent folder. You can comment out or in lines corresponding to the files types you want to get.

```
//savePSB(saveFile)
//saveTIF(saveFile)
//saveJPG(saveFile)
saveJPG({name: folders[i].name, path: fList[0].parent, quality: 90})
savePSD(saveFile)
saveJPG({name: folders[i].name, path: activeDocument.path.parent, quality: 90})
```

Just be aware Photoshop's Photomerge is not fool proof. It does conk out time to time and doesn't solves things correctly. I find that doing those ones manually by using photo merge again but with missing tiles and manually photoshopping those missing tiles back in is the best way around it. 

