# Pride Versioning - pridever 🏳️‍🌈

Idea by [Niki Tonsky](https://mastodon.online/@nikitonsky/113691789641950263).  
A new versioning scheme that is based on the pride of the author.  
https://pridever.org/  

## How it works

Version Number Example: **2.7.123**

Breakdown:

* **Proud version** / first Segment
  * Bump when you are proud of the release.
* **Default version** / second Segment
  * Just normal/okay releases.
* **Shame version** / third Segment
  * Bump when fixing things too embarrassing to admit.

## run

Originally created with this README.md file it is now made with [Pelican](https://getpelican.com/).  

### Development

Install the dependencies and start the local dev-server.  

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd page_generator
pelican -r -l
```

To see the current config: `pelican --print-settings`

### Deployment

```bash
source venv/bin/activate
cd page_generator
pelican content -s publishconf.py
```

## License

Note that the theme `notmyidea` is under the AGPLv3 license.
