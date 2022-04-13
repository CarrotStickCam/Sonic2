#include "global.h"
#include "agb_flash_512k.h"
#include "data.h"

// Only used in here;
extern u32* gUnknown_03005B60;

extern void sub_807234C(u32*);
extern s16 sub_80721A4(void);
extern s16 sub_8071944(void);
extern s16 sub_8071E28(void);

static bool16 sub_80724D4(void);

// Check if the first 10 sectors of flash
// data contain the bytes 0x4547474d
bool16 sub_8063940_HasProfile(void) {
    u32 data[32];
    s16 i;

    if (gUnknown_03001840 & 0x100) {
        return FALSE;
    };

    for (i = 0; i < 10; i++) {
        ReadFlash(i, 0, &data[i * 2], 8);

        if (data[i * 2] ==  0x4547474d) {
            return TRUE;
        }
    } 

    return FALSE;
}

s32 sub_8072474(void) {
    return sub_8071E28();
}

u32 sub_8072484(void) {
    if (!sub_80724D4() && gUnknown_03005B64[0]) {
        return 1;
    } else {
        return sub_8071944();
    }
}


s32 sub_80724B0(void) {
    s16 result = sub_80721A4();

    return result;
}

void sub_80724C0(void) {
    sub_807234C(gUnknown_03005B64);
}

// Returns true if 2 arrays have a different value
// not yet sure what these arrays relate to
static bool16 sub_80724D4(void) {
    u16* pArrayB64 = (u16*)gUnknown_03005B64;
    u16* pArrayB60 = (u16*)gUnknown_03005B60;

    u32 index = 0;
    s32 compare = 444;
    u32 previousIndex;
    
     do {
        if (*pArrayB64 == *pArrayB60) {
            previousIndex = index << 0x10;
            index = 0x10000;
            previousIndex += index;
             
            pArrayB64 = pArrayB64 + 1;
            pArrayB60 = pArrayB60 + 1;
            // Something to do with swapping between signed
            // and 16 and 32bit integers
            index = previousIndex >> 0x10;
        } else {
           return TRUE;
        }
    } while (((s32)previousIndex >> 0x10) < compare);

    return FALSE;
}

// Get the checksum of the given data
UNUSED u32 sub_8072514(u8* data) {
    u32 sum = 0; 
    u32 i;

    for (i = 0; i < 0x374; i += 4) {
        sum += *(u32*)&data[i];
    }

    return sum;
}

// Read flash data at given sector into data
// and verify integrity
bool32 sub_8072538(u8 *data, u16 sectorNum) {
    u32 i;
    u32 sum;
    u32* expected;
    
    ReadFlash(sectorNum, 0, data, 0x378);
    expected = (u32*)&data[0x374];
  
    sum = 0;
    for (i = 0; i < 0x374; i += 4) {
        sum += *(u32 *)&data[i];
    }

    if (*expected != sum) {
        return FALSE;
    }
    
    return TRUE;
}