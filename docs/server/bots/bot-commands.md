!!! info end

    This page lists the Bot commands that are available in-game, based on assigned Account Status, for your EQEmu Server.

## Description

The bot command system has been redesigned and is now a clone of the existing EQEmu command system.

Instead of using the old operator and command tokens #bot command, use the new operator with the new command tokens (i.e., ^command).

A redirect has also been added to the server command interpreter that will allow the use of #bot command..but, only the new command tokens may be used.

Many of the commands have been reviewed, re-coded and improved upon, where possible.

Since bots are an on-going project, some bot commands and features may be programmed into the server code..but, not enabled or fully-realized at this time.

As the actual bot code is updated, more of those commands and features can be enabled, as well as the addition of even more commands.

Please use the ^findaliases command to locate abridged versions of command names.

Using the 'help' or 'usage' argument after a command will show the proper formatting and available options for it.

## Actionable Bots

With specific exceptions, bot commands are designed to work using an 'actionable' argument.

Some of these actionable arguments also require the use of an 'actionable name' parameter.

The use an 'actionable' bot argument provides much greater flexibility and control over a bot or groups of bots and eliminates the overhead of programming multiple selection criteria into a command.

```text
target - selects target as single bot .. use ^command [target] or imply by empty actionable argument
byname [name] - selects single bot by name
ownergroup - selects all bots in the owner's group;
botgroup [name] - selects members of a bot-group by its name
targetgroup - selects all bots in target's group
namesgroup [name] - selects all bots in name's group
healrotation [name] - selects all member and target bots of a heal rotation where name is a member
healrotationmembers [name] - selects all member bots of a heal rotation where name is a member
healrotationtargets [name] - selects all target bots of a heal rotation where name is a member
spawned - selects all spawned bots
all - selects all spawned bots .. argument use indicates en masse database updating
```

Only those bots owned by the commanding player can be selected for any bot command use.

## Example

```text
Usage: (<friendly_target>) ^follow ([option: reset]) [actionable: byname | ownergroup | botgroup | namesgroup | healrotation | spawned] ([actionable_name])
```

* `^follow reset spawned` - resets all spawned bots to follow their default assignments
* `^follow byname Jojo` - Set the bot 'Jojo' to follow the selected friendly target
* `^follow botgroup Mybotgroup` - Sets all spawned members of the bot-group 'Mybotgroup' to follow the selected friendly target
* `^follow ownergroup` - Sets all bots within the owner's group to follow the selected friendly target

Target selection is optional if the argument preceding the command is enclosed in parentheses. In this case, an omitted actionable argument should default to the bot's owner.

If there is no argument preceding the command, then the selected target is not required, and hence, ignored.

Optional 'options' and 'actionable' arguments are also enclosed within parentheses.





| Command                       | Description                                                                                                      | Aliases                               |
|:------------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| ^actionable                   | Lists actionable command arguments and use descriptions                                                          |                                       |
| ^applypoison                  | Applies cursor-held poison to a rogue bot's weapon                                                               | ap                                    |
| ^attack                       | Orders bots to attack a designated target                                                                        | atk                                   |
| ^behindmob                    | Toggles whether or not your bot tries to stay behind a mob                                                       | bh                                    |
| ^blockedbuffs                 | Set, view and clear blocked buffs for the selected bot(s)                                                        | bb                                    |
| ^blockedpetbuffs              | Set, view and clear blocked pet buffs for the selected bot(s)                                                    | bpb                                   |
| ^bot                          | Lists the available bot management [subcommands]                                                                 | b                                     |
| ^botappearance                | Lists the available bot appearance [subcommands]                                                                 | app, appearance                       |
| ^botbeardcolor                | Changes the beard color of a bot                                                                                 | bc, beardcolor                        |
| ^botbeardstyle                | Changes the beard style of a bot                                                                                 | beardstyle                            |
| ^botcamp                      | Orders a bot(s) to camp                                                                                          | camp                                  |
| ^botclone (Disabled)          | Creates a copy of a bot                                                                                          | clone                                 |
| ^botcreate                    | Creates a new bot                                                                                                | create                                |
| ^botdelete                    | Deletes all record of a bot                                                                                      | delete                                |
| ^botdetails                   | Changes the Drakkin details of a bot                                                                             | details                               |
| ^botdyearmor                  | Changes the color of a bot's (bots') armor                                                                       | dyearmor                              |
| ^boteyes                      | Changes the eye colors of a bot                                                                                  | eyes                                  |
| ^botface                      | Changes the facial appearance of your bot                                                                        | face                                  |
| ^botfollowdistance            | Changes the follow distance(s) of a bot(s)                                                                       | followd, followdistance               |
| ^bothaircolor                 | Changes the hair color of a bot                                                                                  | hc, haircolor                         |
| ^bothairstyle                 | Changes the hairstyle of a bot                                                                                   | hs, hairstyle                         |
| ^botheritage                  | Changes the Drakkin heritage of a bot                                                                            | her, heritage                         |
| ^botinspectmessage (Disabled) | Changes the inspect message of a bot                                                                             | inspect                               |
| ^botlist                      | Lists the bots that you own                                                                                      | list                                  |
| ^botreport                    | Orders a bot to report its readiness                                                                             | report, health, mana                  |
| ^botsettings                  | Lists settings related to spell types and bot combat                                                             | settings, bs                          |
| ^botspawn                     | Spawns a created bot                                                                                             | spawn                                 |
| ^botstance                    | Changes the stance of a bot                                                                                      | stance                                |
| ^botstopmeleelevel            | Sets the level a caster or spell-casting fighter bot will stop melee combat                                      | sml                                   |
| ^botsuffix (Disabled)         | Sets a bots suffix                                                                                               | suffix                                |
| ^botsummon                    | Summons bot(s) to your location                                                                                  | summon                                |
| ^botsurname                   | Sets a bots surname (last name)                                                                                  | surname                               |
| ^bottattoo                    | Changes the Drakkin tattoo of a bot                                                                              | tattoo                                |
| ^bottitle                     | Sets a bots title                                                                                                | title                                 |
| ^bottogglehelm (Disabled)     | Toggles the helm visibility of a bot between shown and hidden                                                    | helm, togglehelm, bth                 |
| ^bottoggleranged              | Toggles a ranged bot between melee and ranged weapon use                                                         | btr, toggleranged                     |
| ^botupdate                    | Updates a bot to reflect any level changes that you have experienced                                             | update                                |
| ^botwoad                      | Changes the Barbarian woad of a bot                                                                              | woad                                  |
| ^cast                         | Tells the first found specified bot to cast the given spell type, spell ID or AA ID                              |                                       |
| ^classracelist                | Lists the classes and races and their appropriate IDs                                                            | crl                                   |
| ^clickitem                    | Orders the specified bot(s) to click the item in the provided inventory slot.                                    | click, ci                             |
| ^copysettings                 | Copies settings from one bot to another                                                                          | copy                                  |
| ^defaultsettings              | Restores a bot back to default settings                                                                          | default                               |
| ^depart                       | Orders a bot to open a magical doorway to a specified destination                                                | dep                                   |
| ^discipline                   | Uses aggressive/defensive disciplines or can specify spell ID                                                    | disc                                  |
| ^distanceranged               | Controls the range casters and ranged will try to stay away from a mob                                           | distance, dr                          |
| ^enforcespellsettings         | Toggles your Bot to cast only spells in their spell settings list.                                               | enforce                               |
| ^findaliases                  | Find available aliases for a bot command                                                                         | alias                                 |
| ^follow                       | Orders bots to follow a designated target (option 'chain' auto-links eligible spawned bots)                      |                                       |
| ^guard                        | Orders bots to guard their current positions                                                                     |                                       |
| ^help                         | List available commands and their description - specify partial command as argument to search                    | ?                                     |
| ^hold                         | Prevents a bot from attacking until released                                                                     |                                       |
| ^illusionblock                | Control whether or not illusion effects will land on the bot if casted by another player or bot                  | ib                                    |
| ^inventory                    | Lists the available bot inventory [subcommands]                                                                  | inv                                   |
| ^inventorygive                | Gives the item on your cursor to a bot                                                                           | invgive, ig                           |
| ^inventorylist                | Lists all items in a bot's inventory                                                                             | invlist, il                           |
| ^inventoryremove              | Removes an item from a bot's inventory                                                                           | invremove, invrem, ir                 |
| ^inventorywindow              | Displays all items in a bot's inventory in a pop-up window                                                       | invwindow, iw                         |
| ^itemuse                      | Elicits a report from spawned bots that can use the item on your cursor with filterable options                  | iu                                    |
| ^maxmeleerange                | Toggles whether your bot is at max melee range or not. This will disable all special abilities, including taunt. | mmr                                   |
| ^owneroption                  | Sets options available to bot owners                                                                             | oo                                    |
| ^pet                          | Lists the available bot pet [subcommands]                                                                        | p                                     |
| ^petgetlost                   | Orders a bot to remove its summoned pet                                                                          | pgl                                   |
| ^petremove                    | Orders a bot to remove its charmed pet                                                                           | prem                                  |
| ^petsettype                   | Orders a Magician bot to use a specified pet type                                                                | pset, pst                             |
| ^picklock (Disabled)          | Orders a capable bot to pick the lock of the closest door                                                        | pl                                    |
| ^pickpocket (Disabled)        | Orders a capable bot to pickpocket a NPC                                                                         | pp                                    |
| ^precombat                    | Sets flag used to determine pre-combat behavior                                                                  | pc                                    |
| ^pull                         | Orders a designated bot to 'pull' an enemy                                                                       |                                       |
| ^release                      | Releases a suspended bot's AI processing (with hate list wipe)                                                   |                                       |
| ^setassistee                  | Sets your target to be the person your bots assist. Bots will always assist you before others                    | assistee                              |
| ^sithppercent                 | HP threshold for a bot to start sitting in combat if allowed                                                     | sithp                                 |
| ^sitincombat                  | Toggles whether or a not a bot will attempt to med or sit to heal in combat                                      | sic                                   |
| ^sitmanapercent               | Mana threshold for a bot to start sitting in combat if allowed                                                   | sitmana                               |
| ^spellaggrochecks             | Toggles whether or not bots will cast a spell type if they think it will get them aggro                          | aggrocheck, aggrochecks               |
| ^spellannouncecasts           | Turn on or off cast announcements by spell type                                                                  | announcecast, announcecasts, announce |
| ^spelldelays                  | Controls the delay between casts for a specific spell type                                                       | delay, delays                         |
| ^spellengagedpriority         | Controls the order of casts by spell type when engaged in combat                                                 | engagedpriority, engagedp             |
| ^spellholds                   | Controls whether a bot holds the specified spell type or not                                                     | holds, sholds                         |
| ^spellidlepriority            | Controls the order of casts by spell type when out of combat                                                     | idlepriority, idlep                   |
| ^spellinfo                    | Opens a dialogue window with spell info                                                                          | sinfo                                 |
| ^spellmaxhppct                | Controls at what HP percent a bot will start casting different spell types                                       | maxhp                                 |
| ^spellmaxmanapct              | Controls at what mana percent a bot will start casting different spell types                                     | maxmana                               |
| ^spellmaxthresholds           | Controls the maximum target HP threshold for a spell to be cast for a specific type                              | maxthreshold, maxthresholds, maxt     |
| ^spellminhppct                | Controls at what HP percent a bot will stop casting different spell types                                        | minhp                                 |
| ^spellminmanapct              | Controls at what mana percent a bot will stop casting different spell types                                      | minmana                               |
| ^spellminthresholds           | Controls the minimum target HP threshold for a spell to be cast for a specific type                              | minthreshold, minthresholds, mint     |
| ^spellpursuepriority          | Controls the order of casts by spell type when pursuing in combat                                                | pursuepriority, pursuep               |
| ^spellresistlimits            | Controls the resist limits for bots to cast spells on their target                                               | resistlimit, resistlimits             |
| ^spells                       | Lists all Spells learned by the Bot.                                                                             |                                       |
| ^spellsettings                | Lists a bot's spell setting entries                                                                              | ss                                    |
| ^spellsettingsadd             | Add a bot spell setting entry                                                                                    | ssa                                   |
| ^spellsettingsdelete          | Delete a bot spell setting entry                                                                                 | ssd                                   |
| ^spellsettingstoggle          | Toggle a bot spell use                                                                                           | sst                                   |
| ^spellsettingsupdate          | Update a bot spell setting entry                                                                                 | ssu                                   |
| ^spelltargetcount             | Sets the required target amount for group/AE spells by spell type                                                | targetcount, tc                       |
| ^spelltypeids                 | Lists spelltypes by ID                                                                                           | stids                                 |
| ^spelltypenames               | Lists spelltypes by shortname                                                                                    | stnames                               |
| ^suspend                      | Suspends a bot's AI processing until released                                                                    |                                       |
| ^taunt                        | Toggles taunt use by a bot                                                                                       |                                       |
| ^timer (Disabled)             | Checks or clears timers of the chosen type.                                                                      |                                       |
| ^track                        | Orders a capable bot to track enemies                                                                            |                                       |
| ^viewcombos                   | Views bot race class combinations                                                                                | vc                                    |

