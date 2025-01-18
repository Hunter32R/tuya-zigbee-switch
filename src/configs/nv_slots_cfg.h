
#define MAX_SWITCH_CLUSTERS 5
#define MAX_RELAY_CLUSTERS 5


#define NV_ITEM_ZCL_SWITCH_CONFIG(endpoint)    (NV_ITEM_APP_GP_TRANS_TABLE + endpoint)    // endpoint starts from 1, see sdk/proj/drivers/drv_nv.h

#define NV_ITEM_ZCL_RELAY_CONFIG(endpoint)    (NV_ITEM_ZCL_SWITCH_CONFIG(MAX_SWITCH_CLUSTERS) + endpoint - MAX_SWITCH_CLUSTERS)

#define NV_ITEM_ZCL_DEVICE_CONFIG        NV_ITEM_ZCL_RELAY_CONFIG(MAX_RELAY_CLUSTERS) + 1