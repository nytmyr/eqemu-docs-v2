# Macros

| Useful Macros | Description                                            | Link                |
|:--------------|:-------------------------------------------------------|:--------------------------------|
| DoCombine     | Automatically combines a recipe until out of materials | https://cdn.discordapp.com/attachments/1007081443119353897/1276730759146770464/DoCombine.mac?ex=68f1aaad&is=68f0592d&hm=bf877de8e110e3ce1c9aad6817a7dcc8c2abe07c8e5258423a3ba40cee8498d7& |
| AutoForage    | Automatically forages for you                          | https://cdn.discordapp.com/attachments/1007081443119353897/1361779589298524361/AutoForage.mac?ex=68f14212&is=68eff092&hm=af56e4aa33231fffc0bc13b33237b1f06bb3e33fff1be2706a1b420377f54a43& |

## Raid Setup Macro
### These are Macros for easy spawn, invite and grouping of raids for boxes and bots.
- Use `RaidSetupForRaidLeader.mac` on your main box (the one that is going to be the raid leader and doing all the inviting)
- Use `BoxSpawnRaidBots.mac` for any secondary boxes with bots that need to be spawned and invited, be sure to rename this appropriately.
### Instructions inside so read carefully
- Type names exactly as they appear, do not use all lowercase. If the name is `Warbot`, `warbot` will not work.

**Added samples that I use to spawn bots. Bones is my main that is the raid leader, Bedazz is the boxed character.**

| Sample Macros | Link                                                                                                                           |
|:------|:-------------------------------------------------------------------------------------------------------------------------------|
| Empty Raid Leader Macro | [RaidSetupForRaidLeader.mac](<https://drive.google.com/file/d/1FRGaJ9naoWl-zIQGroVNQxsjtqvk38NV/view?usp=drive_link>)          |
| Empty Box Macro | [BoxSpawnRaidBots.mac](<https://drive.google.com/file/d/1l3c4zqDVGv2rzUBk607mnw6XFlFDyWD0/view?usp=drive_link>)                |
| Sample Raid Leader Macro For Bones | [RaidSetupForRaidLeader.mac (Bones)](<https://drive.google.com/file/d/1r5vEfKy3Fb_Ka0i0FfIYLHdbQ_k6Yotw/view?usp=drive_link>)  |
| Sample Box Macro For Bedazz | [BedazzSpawnRaidBots.mac](<https://drive.google.com/file/d/1W7AG5pcHZKLE8WxgF31S8vbHKUeCQBAN/view?usp=drive_link>)             |

### Tip
You can rename these macros any way you'd like to have different setups.

Say you want to have an alternative raid setup for your ranger bot raid. We'll pretend your main box character is named `Bones` and your alt box is named `Bedazz` and we want to name the macro `BonesRangerRaidSetup` and the box's macro as `BedazzSpawnRangerRaidBots`.
- Name the macros accordingly and change all the bots as needed in the macro
- On `BonesRangerRaidSetup` change the line:
  `/bct ${ClientPlayer${i}.Arg[1,|]} //mac ${ClientPlayer${i}.Arg[1,|]}SpawnRaidBots`
  to
  `/bct ${ClientPlayer${i}.Arg[1,|]} //mac ${ClientPlayer${i}.Arg[1,|]}SpawnRangerRaidBots`
- On `Bones` type `/mac BonesRangerRaidSetup` and enjoy.