/**
 * Used to store unknown globals defined in iwram and ewram
 * until we can find a better place for them
 */
#ifndef GUARD_DATA_H
#define GUARD_DATA_H

#include "global.h"

// TODO: extract this data
extern union Unk_03002E60 gMapHeaders[];

struct SpriteTables {
    void* animations;
    void* dimentions;
    u16** oamData;
    void* palettes;
    void* graphics;
    void* unk20;
};

extern const struct SpriteTables gSpriteTables;

#endif
