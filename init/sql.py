js_sql = {
    "activities": [
        {
            "alias": "CJ组队瓜分京豆",
            "name": "jd_cjzdgf.js",
            "match_url": "jd_cjhy_activityUrl/wxTeam/activity?activityId=jd_cjhy_activityId",
            "re_url": "(https://.*com)/.*?activityId=(\\w+)",
            "head_url": "wxTeam/activity",
            "type_url": "cj",
            "value1": "export jd_cjhy_activityUrl",
            "value2": "export jd_cjhy_activityId"
        },
        {
            "alias": "JoyJd任务脚本",
            "name": "jd_joyjd_open.js",
            "value1": "export comm_activityIDList",
            "value2": "export comm_endTimeList",
            "value3": "export comm_tasknameList"
        },
        {
            "alias": "通用抽奖机",
            "name": "jd_lottery.js",
            "match_url": "https://jdjoy.jd.com/module/task/draw/get?configCode=JD_Lottery",
            "re_url": "configCode=(\\w+)",
            "head_url": "module/task",
            "value1": "export JD_Lottery"
        },
        {
            "alias": "JOY通用开卡活动",
            "name": "jd_joyopen.js",
            "cutting": "@",
            "value1": "export JD_JOYOPEN"
        },
        {
            "alias": "关注店铺有礼",
            "name": "jd_wxShopFollowActivity.js",
            "match_url": "jd_wxShopFollowActivity_activityUrl",
            "re_url": "(https://.*?activityId=\\w+.*)",
            "head_url": "wxShopFollowActivity/activity",
            "value1": "export jd_wxShopFollowActivity_activityUrl"
        },
        {
            "alias": "LZ刮刮乐抽奖通用活动-加密",
            "name": "jd_drawCenter.js",
            "match_url": "https://lzkj-isv.isvjd.com/drawCenter/activity/entry.html?activityId=jd_drawCenter_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "drawCenter/activity",
            "value1": "export jd_drawCenter_activityId"
        },
        {
            "alias": "组队瓜分京豆",
            "name": "jd_zdjr.js",
            "match_url": "jd_zdjr_activityUrl/wxTeam/activity?activityId=jd_zdjr_activityId",
            "re_url": "(https://.*?com).*?activityId=(\\w+)",
            "head_url": "wxTeam/activity",
            "value1": "export jd_zdjr_activityUrl",
            "value2": "export jd_zdjr_activityId"
        },
        {
            "alias": "PKC-特效关注有礼",
            "name": "jd_txgzyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopGift/activity?activityId=PKC_TXGZYL",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopGift/activity",
            "value1": "export PKC_TXGZYL"
        },
        {
            "alias": "入会开卡领取礼包通用",
            "name": "jd_OpenCard_Force.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxInviteActivity/openCard/invitee/442818?activityId=VENDER_ID",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxInviteActivity/openCard",
            "value1": "export VENDER_ID"
        },
        {
            "alias": "大牌联合通用开卡",
            "name": "jd_opencardDPLHTY.js",
            "match_url": "https://jinggengjcq-isv.isvjcloud.com/jdbeverage/pages/oC202301010wee/oC202301010wee?actId=DPLHTY",
            "re_url": "actId=(\\w+)",
            "head_url": "jdbeverage/pages",
            "value1": "export DPLHTY"
        },
        {
            "alias": "微定制瓜分京豆-加密",
            "name": "jd_wdz.js",
            "match_url": "jd_wdz_activityUrljd_wdz_activityUrl/microDz/invite/activity/wx/view/index/8882761?activityId=jd_wdz_activityId",
            "re_url": "(https://.*?com).*?activityId=(\\w+)",
            "head_url": "microDz/invite",
            "value1": "export jd_wdz_activityUrl",
            "value2": "export jd_wdz_activityId"
        },
        {
            "alias": "盲盒任务抽京豆",
            "name": "jd_mhtask.js",
            "value1": "export jd_mhurlList"
        },
        {
            "alias": "砍价免费拿",
            "name": "jd_kanjia.js",
            "value1": "export actId",
            "value2": "export packetId"
        },
        {
            "alias": "粉丝互动通用活动",
            "name": "jd_wxFansInterActionActivity.js",
            "match_url": "https://lzkjdz-isv.isvjd.com/wxFansInterActionActivity/activity?activityId=jd_wxFansInterActionActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxFansInterActionActivity/activity",
            "value1": "export jd_wxFansInterActionActivity_activityId"
        },
        {
            "alias": "读秒拼手速通用活动",
            "name": "jd_wxSecond.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxSecond/activity?activityId=jd_wxSecond_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxSecond/activity",
            "value1": "export jd_wxSecond_activityId"
        },
        {
            "alias": "购物车锦鲤通用活动",
            "name": "jd_wxCartKoi.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxCartKoi/cartkoi/activity?activityId=jd_wxCartKoi_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCartKoi/cartkoi",
            "value1": "export jd_wxCartKoi_activityId"
        },
        {
            "alias": "集卡抽奖通用活动",
            "name": "jd_wxCollectCard.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxCollectCard/activity/activity?activityId=jd_wxCollectCard_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCollectCard/activity",
            "value1": "export jd_wxCollectCard_activityId"
        },
        {
            "alias": "邀好友赢大礼",
            "name": "jd_inviteFriendsGift.py",
            "match_url": "https://prodev.m.jd.com/mall/active/index.html?code=jd_inv_authorCode",
            "re_url": "code=(\\w+)",
            "head_url": "mall/active",
            "value1": "export jd_inv_authorCode"
        },
        {
            "alias": "店铺签到",
            "name": "jd_dpqd.js",
            "match_url": "https://h5.m.jd.com/babelDiy/Zeus/2PAAf74aG3D61qvfKUM5dxUssJQ9/index.html?token=DPQDTK",
            "re_url": "token=(\\w+)",
            "cutting": "&",
            "head_url": "babelDiy/Zeus",
            "value1": "export DPQDTK"
        },
        {
            "alias": "M幸运抽奖",
            "name": "m_jd_wx_luckDraw.js",
            "match_url": "M_WX_LUCK_DRAW_URL",
            "head_url": "lzclient",
            "re_url": ".*",
            "value1": "export M_WX_LUCK_DRAW_URL"
        },
        {
            "alias": "M集卡抽奖",
            "name": "m_jd_wx_collectCard.js",
            "match_url": "M_WX_COLLECT_CARD_URL",
            "re_url": ".*",
            "head_url": "wxCollectCard/activity",
            "value1": "export M_WX_COLLECT_CARD_URL"
        },
        {
            "alias": "M关注有礼",
            "name": "m_jd_follow_shop.js",
            "match_url": "https://shop.m.jd.com/shop/lottery?shopId=#0&venderId=#1",
            "re_url": "shopId=(\\w+)&venderId=(\\w+)",
            "head_url": "shop/lottery",
            "cutting": "_",
            "value1": "export M_FOLLOW_SHOP_ARGV"
        },
        {
            "alias": "M收藏有礼",
            "name": "m_jd_fav_shop_gift.js",
            "value1": "export M_FAV_SHOP_ARGV"
        },
        {
            "alias": "M加购有礼",
            "name": "m_jd_wx_addCart.js",
            "match_url": "M_WX_ADD_CART_URL",
            "re_url": ".*",
            "head_url": "wxCollectionActivity/activity",
            "value1": "export M_WX_ADD_CART_URL"
        },
        {
            "alias": "LZ让福袋飞",
            "name": "jd_wxUnPackingActivity.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxUnPackingActivity/activity/f35ee5d852ec4877bf59bc556fcbe07b?activityId=jd_wxUnPackingActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxUnPackingActivity/activity",
            "value1": "export jd_wxUnPackingActivity_activityId"
        },
        {
            "alias": "微定制瓜分福袋-加密",
            "name": "jd_wdzfd.js",
            "match_url": "jd_wdzfd_activityUrl/microDz/invite/openLuckBag/wx/view/index/8882761?activityId=jd_wdzfd_activityId",
            "re_url": "(https://.*?com).*?activityId=(\\w+)",
            "head_url": "microDz/invite",
            "value1": "export jd_wdzfd_activityUrl",
            "value2": "export jd_wdzfd_activityId"
        },
        {
            "alias": "店铺抽奖通用活动-加密",
            "name": "jd_luck_draw.js",
            "match_url": "LUCK_DRAW_URL",
            "re_url": ".*",
            "head_url": "lzclient|wxDrawActivity/activity",
            "value1": "export LUCK_DRAW_URL"
        },
        {
            "alias": "M老虎机抽奖",
            "name": "m_jd_wx_centerDraw.js",
            "match_url": "M_WX_CENTER_DRAW_URL",
            "re_url": ".*",
            "head_url": "drawCenter/activity",
            "value1": "export M_WX_CENTER_DRAW_URL"
        },
        {
            "alias": "cjhy幸运抽大奖通用活动",
            "name": "jd_cjhy_wxDrawActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxDrawActivity/activity?activityId=jd_cjhy_wxDrawActivity_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxDrawActivity/activity",
            "value1": "export jd_cjhy_wxDrawActivity_Id"
        },
        {
            "alias": "lzkj幸运抽大奖通用活动",
            "name": "jd_lzkj_wxDrawActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/lzclient/1685415463857/cjwx/common/entry.html?activityId=jd_lzkj_wxDrawActivity_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "lzclient",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxDrawActivity_Id"
        },
        {
            "alias": "jinggeng邀请入会有礼",
            "name": "jd_jinggengInvite.py",
            "match_url": "https://jinggeng-isv.isvjcloud.com/ql/front/showInviteJoin?id=#0&user_id=#1",
            "re_url": "activityId=(\\w+)",
            "head_url": "ql/front/showInviteJoin",
            "cutting": "&",
            "value1": "export jinggengInviteJoin"
        },
        {
            "alias": "LZ店铺游戏",
            "name": "jd_wxgame.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxgame/activity?activityId=jd_wxgame_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxgame/activity",
            "value1": "export jd_wxgame_activityId"
        },
        {
            "alias": "分享有礼-加密",
            "name": "jd_wxShareActivity.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxShareActivity/activity?activityId=jd_wxShareActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShareActivity/activity",
            "value1": "export jd_wxShareActivity_activityId"
        },
        {
            "alias": "店铺特效关注有礼-监控脚本",
            "name": "jd_wxShopGift.py",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopGift/activity?activityId=jd_wxShopGiftId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopGift/activity",
            "value1": "export jd_wxShopGiftId"
        },
        {
            "alias": "通用开卡-joinCommon系列",
            "name": "jd_joinCommon_opencard.py",
            "match_url": "https://lzdz1-isv.isvjcloud.com/m/unite/dzlh0001?activityId=#0&venderId=#1",
            "re_url": "activityId=(\\w+)&venderId=(\\d+)",
            "head_url": "wxShopGift/activity|m/unite",
            "cutting": "&",
            "value1": "export jd_joinCommonId"
        },
        {
            "alias": "加购有礼通用",
            "name": "jd_wxCollectionActivity.js",
            "match_url": "jd_wxCollectionActivity_activityUrl",
            "re_url": ".*",
            "head_url": "wxCollectionActivity/activity",
            "value1": "export jd_wxCollectionActivity_activityUrl"
        },
        {
            "alias": "M盖楼领奖",
            "name": "m_jd_wx_buildDraw.js",
            "match_url": "M_WX_BUILD_DRAW_URL",
            "re_url": ".*",
            "head_url": "wxBuildActivity/activity",
            "value1": "export M_WX_BUILD_DRAW_URL"
        },
        {
            "alias": "店铺会员礼包-JK",
            "name": "jd_shopCollectGift.py",
            "match_url": "https://shop.m.jd.com/shop/home?shopId=jd_shopCollectGiftId",
            "re_url": "shopId=(\\w+)",
            "head_url": "shop/home",
            "value1": "export jd_shopCollectGiftId"
        },
        {
            "alias": "M关注有礼无线",
            "name": "m_jd_wx_shopGift.js",
            "match_url": "M_WX_SHOP_GIFT_URL",
            "re_url": ".*",
            "head_url": "wxShopGift/activity",
            "value1": "export M_WX_SHOP_GIFT_URL"
        },
        {
            "alias": "M等级/生日礼包",
            "name": "m_jd_wx_levelBirth.js",
            "match_url": "M_WX_LEVEL_BIRTH_URL",
            "re_url": ".*",
            "head_url": "mc/wxMcLevelAndBirthGifts",
            "value1": "export M_WX_LEVEL_BIRTH_URL"
        },
        {
            "alias": "M读秒手速",
            "name": "m_jd_wx_secondDraw.js",
            "match_url": "M_WX_SECOND_DRAW_URL",
            "re_url": ".*",
            "head_url": "wxSecond/activity",
            "value1": "export M_WX_SECOND_DRAW_URL"
        },
        {
            "alias": "生日礼包和会员等级礼包",
            "name": "jd_wxMcLevelAndBirthGifts.js",
            "match_url": "jd_wxMcLevelAndBirthGifts_activityUrl/mc/wxMcLevelAndBirthGifts/activity?activityId=jd_wxMcLevelAndBirthGifts_activityId",
            "re_url": "(https://.*?com).*?activityId=(\\w+)",
            "head_url": "mc/wxMcLevelAndBirthGifts",
            "value1": "export jd_wxMcLevelAndBirthGifts_activityUrl",
            "value2": "export jd_wxMcLevelAndBirthGifts_activityId"
        },
        {
            "alias": "LZ盖楼有礼",
            "name": "jd_wxBuildActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxBuildActivity/activity?activityId=jd_wxBuildActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxBuildActivity/activity",
            "value1": "export jd_wxBuildActivity_activityId"
        },
        {
            "alias": "完善信息有礼",
            "name": "jd_completeInfoActivity.js",
            "match_url": "jd_completeInfoActivity_activityUrl/wx/completeInfoActivity/view/activity?activityId=jd_completeInfoActivity_activityId&venderId=jd_completeInfoActivity_venderId",
            "re_url": "(https://.*?com).*?activityId=(\\w+)&venderId=(\\d+)",
            "head_url": "wx/completeInfoActivity",
            "value1": "export jd_completeInfoActivity_activityUrl",
            "value2": "export jd_completeInfoActivity_activityId",
            "value3": "export jd_completeInfoActivity_venderId"
        },
        {
            "alias": "生日礼包-JK",
            "name": "jd_wxBirthGifts.py",
            "match_url": "https://cjhy-isv.isvjcloud.com/mc/wxMcLevelAndBirthGifts/activity?activityId=jd_wxBirthGiftsId",
            "re_url": "activityId=(\\w+)",
            "head_url": "mc/wxMcLevelAndBirthGifts",
            "value1": "export jd_wxBirthGiftsId"
        },
        {
            "alias": "通用开卡-shopLeague系列脚本",
            "name": "jd_shopLeague_opencard.py",
            "match_url": "https://lzdz1-isv.isvjd.com/dingzhi/shop/league/activity?activityId=jd_shopLeagueId",
            "re_url": "activityId=(\\w+)",
            "head_url": "dingzhi/shop",
            "value1": "export jd_shopLeagueId"
        },
        {
            "alias": "M关注抽奖",
            "name": "m_jd_wx_followDraw.js",
            "match_url": "M_WX_FOLLOW_DRAW_URL",
            "re_url": ".*",
            "head_url": "wxShopFollowActivity/activity",
            "value1": "export M_WX_FOLLOW_DRAW_URL"
        },
        {
            "alias": "分享有礼",
            "name": "jd_share.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxShareActivity/activity?activityId=jd_fxyl_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShareActivity/activity",
            "value1": "export jd_fxyl_activityId"
        },
        {
            "alias": "知识超人",
            "name": "jd_wxKnowledgeActivity.js",
            "match_url": "jd_wxKnowledgeActivity_activityUrl",
            "re_url": ".*",
            "head_url": "wxKnowledgeActivity/activity",
            "value1": "export jd_wxKnowledgeActivity_activityUrl"
        },
        {
            "alias": "通用游戏任务",
            "name": "jd_game.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxgame/activity?activityId=WXGAME_ACT_ID",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxgame/activity",
            "value1": "export WXGAME_ACT_ID"
        },
        {
            "alias": "cjhy七日签到",
            "name": "jd_cjhy_sevenDay.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/sign/sevenDay/signActivity?activityId=jd_cjhy_sevenDay_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/sevenDay",
            "type_url": "cj",
            "cutting": "&",
            "value1": "export jd_cjhy_sevenDay_ids"
        },
        {
            "alias": "cjhy签到有礼",
            "name": "jd_cjhy_signActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/sign/signActivity?activityId=jd_cjhy_signActivity_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/signActivity",
            "value1": "export jd_cjhy_signActivity_ids"
        },
        {
            "alias": "lzkj七日签到",
            "name": "jd_lzkj_sevenDay.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/sign/sevenDay/signActivity?activityId=jd_lzkj_sevenDay_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/sevenDay",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_sevenDay_ids"
        },
        {
            "alias": "lzkj签到有礼",
            "name": "jd_lzkj_signActivity2.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/sign/signActivity2?activityId=jd_lzkj_signActivity2_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/signActivity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_signActivity2_ids"
        },
        {
            "alias": "lzkj盖楼有礼",
            "name": "jd_lzkj_wxBuildActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxBuildActivity/activity?activityId=jd_lzkj_wxBuildActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxBuildActivity/activity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxBuildActivity_activityId"
        },
        {
            "alias": "cjhy每日抢",
            "name": "jd_cjhy_daily.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/activity/daily/wx/indexPage1?activityId=jd_cjhy_daily_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "activity/daily",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_daily_ids"
        },
        {
            "alias": "品类联合-通用脚本",
            "name": "jd_lzdz_categoryUnion.js",
            "match_url": "https://lzdz-isv.isvjd.com/categoryUnion/categoryUnionActivity?code=categoryUnion_activityId",
            "re_url": "code=(\\w+)",
            "head_url": "categoryUnion/categoryUnionActivity",
            "value1": "export categoryUnion_activityId"
        },
        {
            "alias": "cjhy生日礼",
            "name": "jd_cjhy_wxMcLevelAndBirthGifts.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/mc/wxMcLevelAndBirthGifts/activity?activityId=jd_cjhy_wxMcLevelAndBirthGifts_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "mc/wxMcLevelAndBirthGifts",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxMcLevelAndBirthGifts_ids"
        },
        {
            "alias": "加购有礼-监控脚本",
            "name": "jd_wxCollectionActivity.py",
            "match_url": "jd_wxCollectionActivityUrl",
            "re_url": ".*",
            "head_url": "wxCollectionActivity/activity",
            "value1": "export jd_wxCollectionActivityUrl"
        },
        {
            "alias": "CJ每日抢好礼通用活动",
            "name": "jd_cjdaily.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/activity/daily/wx/indexPage?activityId=jd_cjdaily_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "activity/daily",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjdaily_activityId"
        },
        {
            "alias": "CJ关注店铺有礼",
            "name": "jd_cjwxShopFollowActivity.js",
            "match_url": "https://cjhydz-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=jd_cjwxShopFollowActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopFollowActivity/activity",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjwxShopFollowActivity_activityId"
        },
        {
            "alias": "LZ每日抢好礼通用活动",
            "name": "jd_daily.js",
            "match_url": "https://lzkj-isv.isvjd.com/activity/daily/wx/indexPage?activityId=jd_daily_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "activity/daily",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_daily_activityId"
        },
        {
            "alias": "关注有礼-加密",
            "name": "jd_follow.js",
            "match_url": "https://shop.m.jd.com/shop/lottery?shopId=#0&venderId=#1&channel=406&venderType=1",
            "re_url": "shopId=(\\w+)&venderId=(\\d+)",
            "head_url": "shop/lottery",
            "cutting": "_",
            "value1": "export M_FOLLOW_SHOP_ARGV"
        },
        {
            "alias": "店铺礼包特效",
            "name": "jd_wxShopGift.js",
            "match_url": "jd_wxShopGift_activityUrl",
            "re_url": "(https://.*?activityId=.*)",
            "head_url": "wxShopGift/activity",
            "value1": "export jd_wxShopGift_activityUrl"
        },
        {
            "alias": "lzkj游戏活动",
            "name": "jd_lzkj_wxGameActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxGameActivity/activity/activity?activityId=jd_lzkj_wxGameActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxGameActivity/activity",
            "value1": "export jd_lzkj_wxGameActivity_activityId"
        },
        {
            "alias": "cjhy游戏活动",
            "name": "jd_cjhy_wxGameActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxGameActivity/activity?activityId=jd_cjhy_wxGameActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxGameActivity/activity",
            "cutting": "cj",
            "value1": "export jd_cjhy_wxGameActivity_activityId"
        },
        {
            "alias": "lzkj关注店铺有礼",
            "name": "jd_lzkj_wxShopFollowActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=jd_lzkj_wxShopFollowActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopFollowActivity/activity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxShopFollowActivity_activityId"
        },
        {
            "alias": "lzkj店铺礼包",
            "name": "jd_lzkj_wxShopGift.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopGift/activity?activityId=jd_lzkj_wxShopGift_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopGift/activity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxShopGift_ids"
        },
        {
            "alias": "cjhy店铺礼包",
            "name": "jd_cjhy_wxShopGift.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxShopGift/activity?activityId=jd_cjhy_wxShopGift_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopGift/activity",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxShopGift_ids"
        },
        {
            "alias": "lzkj加购物车抽奖",
            "name": "jd_lzkj_wxCollectionActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxCollectionActivity/activity2?activityId=jd_lzkj_wxCollectionActivityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCollectionActivity/activity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxCollectionActivityId"
        },
        {
            "alias": "收藏大师-幸运抽奖",
            "name": "jd_txzj_lottery.js",
            "match_url": "jd_lottery_activityUrl",
            "re_url": ".*",
            "head_url": "lottery/home",
            "value1": "export jd_lottery_activityUrl"
        },
        {
            "alias": "收藏大师-关注有礼",
            "name": "jd_txzj_collect_item.js",
            "match_url": "jd_collect_item_activityUrl",
            "re_url": ".*",
            "head_url": "collect_item/home",
            "value1": "export jd_collect_item_activityUrl"
        },
        {
            "alias": "收藏大师-关注商品",
            "name": "jd_collect_shop.js",
            "match_url": "jd_collect_shop_activityUrl",
            "re_url": ".*",
            "head_url": "collect_shop/home",
            "value1": "export jd_collect_shop_activityUrl"
        },
        {
            "alias": "收藏大师-加购有礼",
            "name": "jd_txzj_cart_item.js",
            "match_url": "jd_cart_item_activityUrl",
            "re_url": ".*",
            "head_url": "cart_item/home",
            "value1": "export jd_cart_item_activityUrl"
        },
        {
            "alias": "完善信息有礼-JK",
            "name": "jd_wxCompleteInfo.py",
            "match_url": "https://cjhy-isv.isvjcloud.com/wx/completeInfoActivity/view/activity?activityId=#0&venderId=#1",
            "re_url": "activityId=(\\w+)&venderId=(\\w+)",
            "head_url": "wx/completeInfoActivity",
            "cutting": "&",
            "value1": "export jd_wxCompleteInfoId"
        },
        {
            "alias": "盖楼有礼-JK",
            "name": "jd_wxBulidActivity.py",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxBuildActivity/activity?activityId=jd_wxBulidActivityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxBuildActivity/activity",
            "value1": "export jd_wxBulidActivityId"
        },
        {
            "alias": "微定制组队瓜分-JK",
            "name": "jd_wdz.py",
            "match_url": "https://cjhydz-isv.isvjcloud.com/microDz/invite/activity/wx/view/index?activityId=jd_wdz_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "microDz/invite",
            "value1": "export jd_wdz_activityId"
        },
        {
            "alias": "jinggeng组队瓜分",
            "name": "jd_jgzdgf.js",
            "match_url": "jd_jinggengzdfg_url",
            "re_url": ".*",
            "head_url": "ql/front/showPartition",
            "value1": "export jd_jinggengzdfg_url"
        },
        {
            "alias": "M粉丝红包",
            "name": "m_jd_fans_redPackt.js",
            "match_url": "M_FANS_RED_PACKET_URL",
            "re_url": ".*",
            "head_url": "sns",
            "value1": "export M_FANS_RED_PACKET_URL"
        },
        {
            "alias": "邀好友赢大礼",
            "name": "jd_prodev.py",
            "match_url": "https://prodev.m.jd.com/mall/active?code=yhyauthorCode",
            "re_url": "code=(\\w+)",
            "head_url": "mall/active",
            "value1": "export yhyauthorCode"
        },
        {
            "alias": "品类联合任务",
            "name": "jd_categoryUnion.js",
            "match_url": "https://lzdz-isv.isvjd.com/categoryUnion/categoryUnionActivity?code=jd_categoryUnion_activityId",
            "re_url": "code=(\\w+)",
            "head_url": "categoryUnion/categoryUnionActivity",
            "value1": "export jd_categoryUnion_activityId"
        },
        {
            "alias": "lzkj_loreal邀请入会有礼",
            "name": "jd_lzkj_loreal_invite.js",
            "match_url": "jd_lzkj_loreal_invite_url",
            "re_url": "(https.*?activityType=10070.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_invite_url"
        },
        {
            "alias": "邀请入会赢好礼·京耕",
            "name": "jd_jinggeng_showInviteJoin.js",
            "match_url": "jd_showInviteJoin_activityUrl",
            "re_url": ".*",
            "head_url": "ql/front/showInviteJoin",
            "value1": "export jd_showInviteJoin_activityUrl"
        },
        {
            "alias": "M组队瓜分",
            "name": "m_jd_wx_team.js",
            "match_url": "M_WX_TEAM_URL",
            "re_url": ".*",
            "head_url": "wxTeam/activity",
            "value1": "export M_WX_TEAM_URL"
        },
        {
            "alias": "M无线游戏",
            "name": "m_jd_wx_game.js",
            "match_url": "M_WX_GAME_URL",
            "re_url": ".*",
            "head_url": "wxGameActivity/activity",
            "value1": "export M_WX_GAME_URL"
        },
        {
            "alias": "M分享有礼",
            "name": "m_jd_wx_share.js",
            "match_url": "M_WX_SHARE_URL",
            "re_url": ".*",
            "head_url": "wxShareActivity/activity",
            "value1": "export M_WX_SHARE_URL"
        },
        {
            "alias": "M打豆豆",
            "name": "m_jd_wx_dadoudou.js",
            "match_url": "M_WX_DADOUDOU_URL",
            "re_url": ".*",
            "head_url": "wxgame/activity",
            "value1": "export M_WX_DADOUDOU_URL"
        },
        {
            "alias": "超级无线店铺签到",
            "name": "jd_sevenDay.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/sign/signActivity?activityId=SEVENDAY_LIST",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/signActivity",
            "value1": "export SEVENDAY_LIST"
        },
        {
            "alias": "jd_lzkjInteract邀请有礼",
            "name": "jd_lzkjInteract.py",
            "match_url": "jd_lzkjInteractUrl",
            "re_url": "(https://.*?activityType=10070.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkjInteractUrl"
        },
        {
            "alias": "店铺左侧刮刮乐",
            "name": "jd_shopDraw.js",
            "match_url": "jd_shopDraw_activityUrl",
            "re_url": ".*",
            "head_url": "shop/lottery",
            "value1": "export jd_shopDraw_activityUrl"
        },
        {
            "alias": "店铺抽奖",
            "name": "jd_shop_draw.js",
            "match_url": "https://shop.m.jd.com/shop/lottery?shopId=jd_shop_draw_ids",
            "re_url": "shopId=(\\w+)",
            "cutting": "&",
            "head_url": "wxDrawActivity/activity",
            "value1": "export jd_shop_draw_ids"
        },
        {
            "alias": "关注有礼-JK",
            "name": "jd_shopFollowGift.py",
            "value1": "export jd_shopFollowGiftId"
        },
        {
            "alias": "店铺抽奖-JK",
            "name": "jd_dpcj.py",
            "match_url": "https://shop.m.jd.com/shop/lottery?shopId=DPCJID",
            "re_url": "shopId=(\\d+)",
            "head_url": "shop/lottery",
            "cutting": "&",
            "value1": "export DPCJID"
        },
        {
            "alias": "lzkj邀请入会有礼",
            "name": "jd_lzkj_interactsaas_yqrhyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityId=jd_lzkj_interactsaas_yqrhyl_activityId",
            "re_url": "activityType=10070.*?activityId=(\\w+)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_interactsaas_yqrhyl_activityId"
        },
        {
            "alias": "入会开卡领取礼包通用",
            "name": "jd_card_force.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxInviteActivity/openCard/invitee/442818?activityId=VENDER_ID",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxInviteActivity/openCard",
            "value1": "export VENDER_ID"
        },
        {
            "alias": "cjhy加购物车抽奖",
            "name": "jd_cjhy_wxCollectionActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxCollectionActivity/activity?activityId=jd_cjhy_wxCollectionActivityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCollectionActivity/activity",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxCollectionActivityId"
        },
        {
            "alias": "cjhy知识超人",
            "name": "jd_cjhy_wxKnowledgeActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxKnowledgeActivity/activity?activityId=jd_cjhy_wxKnowledgeActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxKnowledgeActivity/activity",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxKnowledgeActivity_activityId"
        },
        {
            "alias": "cjhy关注店铺有礼",
            "name": "jd_cjhy_wxShopFollowActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=jd_cjhy_wxShopFollowActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopFollowActivity/activity",
            "type_url":"cj",
            "value1": "export jd_cjhy_wxShopFollowActivity_activityId"
        },
        {
            "alias": "lzkj每日抢",
            "name": "jd_lzkj_daily.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/activity/daily/wx/indexPage?activityId=jd_lzkj_daily_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "activity/daily",
            "type_url": "lz",
            "cutting": "&",
            "value1": "export jd_lzkj_daily_ids"
        },
        {
            "alias": "lzkj知识超人",
            "name": "jd_lzkj_wxKnowledgeActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxKnowledgeActivity/activity?activityId=jd_lzkj_wxKnowledgeActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxKnowledgeActivity/activity",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxKnowledgeActivity_activityId"
        },
        {
            "alias": "邀请好友入会赢好礼-火箭版",
            "name": "jd_prodev.js",
            "match_url": "https://prodev.m.jd.com/mall/active/dVF7gQUVKyUcuSsVhuya5d2XD4F/index.html?code=prodevactCode",
            "re_url": "code=(\\w+)",
            "head_url": "mall/active",
            "value1": "export prodevactCode"
        },
        {
            "alias": "店铺礼包",
            "name": "jd_shopGifts.js",
            "value1": "export jd_shopGifts_ids"
        },
        {
            "alias": "微定制-开福袋",
            "name": "jd_wdz_openLuckBag.js",
            "match_url": "https://cjhydz-isv.isvjcloud.com/microDz/invite/openLuckBag/wx/view/index?activityId=jd_wdz_openLuckBag_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "microDz/invite",
            "value1": "export jd_wdz_openLuckBag_activityId"
        },
        {
            "alias": "组队分豆-瓜分",
            "name": "jd_team_exchange.js",
            "js_level": 4,
            "value1": "export jd_teamAJ",
            "value2": "export jd_teamFLP"
        },
        {
            "alias": "店铺签到转换为json格式",
            "name": "jd_convert_json.py",
            "match_url": "https://h5.m.jd.com/babelDiy/Zeus/2PAAf74aG3D61qvfKUM5dxUssJQ9/index.html?token=ShopToken",
            "re_url": "token=(\\w+)",
            "cutting": "&",
            "level": 6,
            "head_url": "babelDiy/Zeus",
            "value1": "export ShopToken"
        },
        {
            "alias": "加购有礼（超级无线欧莱雅)",
            "name": "jd_lzkj_loreal_cart.js",
            "match_url": "jd_lzkj_loreal_cart_url",
            "re_url": "(https.*?activityType=10024.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_cart_url"
        },
        {
            "alias": "幸运抽奖(超级无线欧莱雅)",
            "name": "jd_lzkj_loreal_draw.js",
            "match_url": "jd_lzkj_loreal_draw_url",
            "re_url": "(https.*?activityType=(?:10020|10021|10026|10031|10063|10080).*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_draw_url"
        },
        {
            "alias": "关注店铺有礼(超级无线欧莱雅)",
            "name": "jd_lzkj_loreal_followShop.js",
            "match_url": "jd_lzkj_loreal_followShop_url",
            "re_url": "(https.*?activityType=10069.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_followShop_url"
        },
        {
            "alias": "lzkj_interactsaas关注商品有礼",
            "name": "jd_lzkj_interactsaas_gzspyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10069&activityId=jd_lzkj_interactsaas_gzspyl_activityId",
            "re_url": "(https.*?activityType=(?:10069|10053).*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_interactsaas_gzspyl_activityId"
        },
        {
            "alias": "jd_lzkjInteract关注有礼",
            "name": "jd_lzkjInteractFollow.py",
            "match_url": "jd_lzkjInteractFollowUrl",
            "re_url": "(https.*?activityType=(?:10069|10053)&templateId=\\w+&activityId=\\w+)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkjInteractFollowUrl"
        },
        {
            "alias": "lzkj_interactsaas加购有礼",
            "name": "jd_lzkj_interactsaas_jgyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10024&activityId=jd_lzkj_interactsaas_jgyl_activityI",
            "re_url": "activityType=10024.*?activityId=(\\w+)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_interactsaas_jgyl_activityId"
        },
        {
            "alias": "lzkj邀请入会有礼",
            "name": "jd_lzkj_interact_yqrhyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10070&activityId=jd_lzkj_interact_yqrhyl_activityId",
            "re_url": "activityType=10070.*?activityId=(\\w+)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_interact_yqrhyl_activityId"
        },
        {
            "alias": "lzkj_interactsaas关注店铺有礼",
            "name": "jd_lzkj_interactsaas_gzyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10069&activityId=jd_lzkj_interactsaas_gzyl_activityId",
            "re_url": "activityType=(?:10069|10053).*?activityId=(\\w+)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_interactsaas_gzyl_activityId"
        },
        {
            "alias": "loreal邀请入会有礼",
            "name": "jd_loreal_interact_yqrhyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10070&activityId=jd_lzkj_interact_yqrhyl_activityId",
            "re_url": "activityType=10070.*?activityId=(\\w+)",
            "head_url": "prod/cc",
            "value1": "export jd_loreal_interact_yqrhyl_activityId"
        },
        {
            "alias": "邀请赢大礼",
            "name": "jd_invite_leaf.js",
            "match_url": "jd_invite_activity_url",
            "re_url": "code=(\\w+)",
            "head_url": "mall/active",
            "value1": "export jd_invite_activity_url"
        },
        {
            "alias": "微定制",
            "name": "jd_cjhydz_microDz.js",
            "match_url": "https://cjhydz-isv.isvjcloud.com/microDz/invite/activity/wx/view/index?activityId=jd_cjhydz_microDz_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "microDz/invite/activity",
            "js_level": 4,
            "value1": "export jd_cjhydz_microDz_Id"
        },
        {
            "alias": "cj组队瓜分",
            "name": "jd_cjhydz_wxTeam.js",
            "match_url": "https://cjhydz-isv.isvjcloud.com/wxTeam/activity?activityId=jd_cjhydz_wxTeam_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxTeam/activity",
            "type_url": "cj",
            "js_level": 4,
            "value1": "export jd_cjhydz_wxTeam_Id"
        },
        {
            "alias": "lz组队瓜分",
            "name": "jd_lzkjdz_wxTeam.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxTeam/activity?activityId=jd_lzkjdz_wxTeam_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxTeam/activity",
            "js_level": 4,
            "type_url": "lz",
            "value1": "export jd_lzkjdz_wxTeam_Id"
        },
        {
            "alias": "微定制-开福袋",
            "name": "jd_openLuckBag.js",
            "match_url": "https://cjhydz-isv.isvjcloud.com/microDz/invite/openLuckBag/wx/view/index?activityId=jd_openLuckBag_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "microDz/invite/openLuckBag",
            "value1": "export jd_openLuckBag_Id"
        },
        {
            "alias": "关注店铺有礼-JK",
            "name": "jd_wxShopFollow.py",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=jd_wxShopFollowId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopFollowActivity/activity",
            "value1": "export jd_wxShopFollowId"
        },
        {
            "alias": "超级无线店铺签到-监控版",
            "name": "jd_sevenDayjk.js",
            "match_url": "jd_sevenDay_activityUrl",
            "re_url": ".*",
            "level": 4,
            "head_url": "babelDiy/Zeus|sign/signActivity|sign/sevenDay",
            "value1": "export jd_sevenDay_activityUrl"
        },
        {
            "alias": "积分兑换京豆 · 超级会员",
            "name": "jd_pointExgBeans.js",
            "match_url": "jd_pointExgBeans_activityUrl",
            "re_url": ".*",
            "level": 4,
            "head_url": "mc/wxPointShopView",
            "value1": "export jd_pointExgBeans_activityUrl"
        },
        {
            "alias": "京东抽奖机加购-KR",
            "name": "jd_lottery_cart.js",
            "cutting": "@",
            "level": 4,
            "value1": "export JD_Lottery_cart"
        },
        {
            "alias": "txzj 签到",
            "name": "jd_txzj_sign_in.js",
            "match_url": "https://txzj-isv.isvjcloud.com/sign_in/home?a=jd_txzj_sign_in_id",
            "re_url": "a=(\\w+)",
            "level": 4,
            "head_url": "sign_in/home",
            "value1": "export jd_txzj_sign_in_id"
        },
        {
            "alias": "签到有礼（超级无线欧莱雅）",
            "name": "jd_lzkj_loreal_daySign.js",
            "match_url": "jd_lzkj_loreal_daySign_url",
            "re_url": "(https.*?activityType=(?:10023|10040).*?activityId=\\w+.*?)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_daySign_url"
        },
        {
            "alias": "关注商品有礼（超级无线欧莱雅）",
            "name": "jd_lzkj_loreal_followGoods.js",
            "match_url": "jd_lzkj_loreal_followGoods_url",
            "re_url": "(https.*?activityType=10053.*?activityId=\\w+.*?)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_followGoods_url"
        },
        {
            "alias": "上上签抽奖（超级无线欧莱雅）",
            "name": "jd_lzkj_loreal_upperSign.js",
            "match_url": "jd_lzkj_loreal_upperSign_url",
            "re_url": "(https.*?activityType=10054.*?activityId=\\w+.*?)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_upperSign_url"
        },
        {
            "alias": "关注店铺有礼（超级无线欧莱雅）",
            "name": "jd_lzkj_loreal_lkFollowShop.js",
            "match_url": "jd_lzkj_loreal_lkFollowShop_ur",
            "re_url": "(https.*?activityType=10069.*?activityId=\\w+.*?)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_lkFollowShop_ur"
        },
        {
            "alias": "签到抽奖（lzkj_loreal）",
            "name": "jd_lzkj_loreal_sign.js",
            "match_url": "jd_lzkj_loreal_sign_url",
            "re_url": "(https.*?activityType=10001.*?activityId=\\w+.*?)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_sign_url"
        }
    ]
}