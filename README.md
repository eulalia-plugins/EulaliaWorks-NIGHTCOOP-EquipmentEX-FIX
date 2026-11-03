# EulaliaWorks NightCoop / Equipment-EX port

Current snapshot: Cyberpunk 2077 **2.5**, NightCoop **0.2.0 beta**, native **R3**, photo receiver **v5.1**, photo attachment candidate **v5.4**.

The normal Equipment-EX outfit bridge has been confirmed working in co-op by Eulalia. Hair and pose synchronization have also been confirmed in the tested setup. **Complete photo-mode EX/facial-accessory visibility is still experimental.** The latest v5.4 spider-accessory correction compiled but has not been visually verified. This is a development release, not a claim that every photo attachment is fixed.

The port reads Equipment-EX's configured outfit rather than relying on whichever visual ItemObject happens to exist under the active camera. It preserves full item identity, prefers a recognized final EX placement slot, transmits exact photo slot mappings through the SDK, and keeps verified remote photo actors simulating while the world remains frozen. R3 also corrects a captured UTF-8 pose-name crash.

**Install requirements:** install the normal NightCoop 0.2.0 build for game 2.5, Equipment-EX 1.2.10 and their dependencies first. This snapshot uses RED4ext, redscript, ArchiveXL, TweakXL, Codeware and Cyber Engine Tweaks. Keep cosmetic mods and their dependencies consistent between participants. Install this port on every participating PC. It does not contain or transfer cosmetic assets.

**Full runtime ZIP:** `NightCoop-EEX-Photo-Current-R3-v5.4.zip` includes the exact patched NightCoop DLL plus the current modified scripts. Close the game, back up the files you are replacing, extract into the active Cyberpunk 2077 folder, and replace matching files. Restart every participant's game. This is an overlay for an existing normal EEX/NightCoop installation, not a full dependency installer.

**Public source ZIP:** `NightCoop-EEX-Photo-Port-Source-v5.4.zip` contains the scripts and native patch recipe, but no NightCoop runtime DLL. With Python 3, run `python native-patch/apply_native_patch.py PATH_TO_STOCK_NIGHTCOOP_DLL --output NightCoop-R3.dll`. It accepts only the exact official input hash, verifies original bytes and the final hash, and writes a NEW output file. It does not install anything. Close the game, back up the existing DLL, manually copy the generated DLL into `red4ext/plugins/NightCoop/` as `NightCoop.dll`, and extract the source ZIP's `r6` and `bin` folders into the game. Developers can also apply the JSON patch recipe through their own tooling.

Merge these three settings into your existing `red4ext/plugins/NightCoop/switches.txt`; the package deliberately does not replace your personal switches file:

```ini
photo_live_pause_all = on
photo_double_place = off
photo_double_respawn = off
```

Expected patched DLL SHA256: `42F531BDF2C7E26948FFF61CACF3990EF15F5F4BB2F7A39C6684768A2045CF80`.
Required official input DLL SHA256: `447EE81CB5200DE2B372372A5C68DD36275C7B172EEEE009F56E5D5D606C55F7`.
Do not apply native offsets to a different NightCoop version. A newer release needs a separate port.

**Known limitations:** photo-mode spider/visor visibility remains unresolved until a successful v5.4 visual test. Three previously logged rejected placements involved a neck piece and two belts; v5.4 does not address those. The photo peer association is conservative but heuristic, particularly with more than two players. The protocol rejects duplicate records, so two copies of the same record in different slots are not supported. SmartFrames synchronization is not implemented. General body UV/mesh compatibility, custom animation availability and missing cosmetic assets are outside this patch.

**Validation:** exact native reader/resolver and slot-selector harnesses: 700 and 109 cases; pose CRC harness: 515 cases; actual LuaJIT controller/protocol tests: 21 protocol cases plus clock, session, malformed-data and peer-selection checks. The latest photo script compiled with the installed scripts and SDK. Reproducing the R3 DLL from the recipe was checked byte-for-byte against the installed DLL. These tests do not establish complete in-game rendering correctness.

There are no log collectors, CMD/PowerShell launchers, personal logs, save files, tattoo edits, cyberware recolors or SDK definition copies in these packages. The runtime ZIP contains a modified NightCoop core DLL; it is not a purely SDK-based addon. The public source bundle omits that DLL. The SDK license alone must not be presented as a license for the core runtime; redistribution permission for that binary has not been established here.

Equipment-EX is by Pavel Siberx and its MIT notice is retained. NightCoop, Cyberpunk and the modding frameworks remain their authors' work. See THIRD-PARTY.md and HOW-IT-WORKS.md. No Discord message or upload is performed by this package.
