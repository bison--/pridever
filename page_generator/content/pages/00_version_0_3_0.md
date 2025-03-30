Title: Pride Versioning 🏳️‍🌈 0.3.0
Date: 2025-03-30 01:42
Category: Version
opengraph_image: pridever.png
URL:
save_as: index.html

## Summary

Given a version number **PROUD.DEFAULT.SHAME**, increment the:

1. PROUD version when you make changes you are really proud of  
2. DEFAULT version when you make a release that's okay
3. SHAME version when you are fixing things that are too embarrassing to admit

Additional labels for pre-release and build metadata are available as extensions to the **PROUD.DEFAULT.SHAME** format.

## How it works

![Diagram with a version number: 2.7.123
First “2” is commented: Proud version. Bump when you are proud of the release
Second “7” is commented: Default version. Just normal/okay releases
Third “123” is commented: Shame version. Bump when fixing things too embarrassing to admit]({static}/images/pridever.png)

Version Number Example: **2.7.123**

Breakdown:

* **Proud version** / first Segment
    * Bump when you are proud of the release.
* **Default version** / second Segment
    * Just normal/okay releases.
* **Shame version** / third Segment
    * Bump when fixing things too embarrassing to admit.

### Increasing the Proud Version

When increasing the **Proud Version** you can start with a blank slate.  
For example:  

Increasing the **Proud Version** on **1.2.3** by **1** would yield **2.0.0**, so you can fully show the proudness of your new version.
