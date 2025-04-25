package com.tuzicao.emeraldknight.kernel;

import java.util.HashMap;
import java.util.LinkedList;

import com.tuzicao.emeraldknight.R;

public class Constant {
    static String BRUCE_STORY_LINE = "bsl";
    static String BRUCE_SHOW_UP = "bsu";
    static String BRUCE_LOVE = "brl";
    static String BRUCE_INTRODUCE = "bri";
    static String OLIVER_STORY_LINE = "osl";
    static String OLIVER_LOVE = "oll";
    static String SINESTRO_STORY_LINE = "ssl";
    static String SINESTRO_LOVE = "sil";
    static String SINESTRO_TAME = "sit";
    static String BARRY_LOVE = "bal";

    static String SWORD_HOT_TIME = "sht";
    static String KNOWLEDGE = "knw";
    static String INTELLIGENCE = "int";
    static String TEMPORARY = "tmp";
    static String PROPS = "pro";
    static String PEGASUS = "pgs";
    static String DRAGON_EGG = "dge";

    static String TEAMMATE = "tmm";
    static int BRUCE_CODE = 1;
    //    static int SINESTRO_CODE = 2;
    static int OLIVER_CODE = 3;
    static int BARRY_CODE = 4;

    static String GAME_OVER = "game over";
    static String FINAL_BATTLE = "final_battle";

    static HashMap<String, String> scene_name = new HashMap<String, String>() {{
        put("1-1", "出发");
        put("1-2", "继续前进");
        put("1-3", "原路返回");
        put("1-4", "就地睡一觉");
        put("1-5", "跟着前进");
        put("1-6", "原地蹲守");
        put("1-7", "不理会");
        put("1-8", "上树跟去看看");
        put("1-9", "呛回去");
        put("1-10", "谢谢他");
        put("1-11", "“你是谁？”");
        put("1-12", "进去");
        put("1-13", "先四下看看");
        put("1-14", "上去敲门");
        put("1-15", "再进森林");
        put("1-16", "去龙骨雪山");
        put("1-17", "回家睡觉");
        put("1-18", "去找卡萝");
        put("1-19", "当然要继续");
        put("1-20", "红晶石");
        put("1-21", "蓝晶石");
        put("1-22", "紫晶石");
        put("1-23", "绿晶石");
        put("1-24", "继续前进");
        put("1-25", "光明符文");
        put("1-26", "大地符文");
        put("1-27", "黑暗符文");
        put("1-28", "雷电符文");
        put("1-29", "推门离开");
        put("1-30", "追上去");
        put("1-31", "四处走走");
        put("1-32", "去追黑影");
        put("1-33", "在湖边休息");
        put("1-34", "用光明术");
        put("1-35", "什么地方");
        put("1-36", "你是什么人？");
        put("1-37", "怎么离开这儿？");
        put("1-38", "你确定吗？");
        put("1-39", "阵眼什么样？");
        put("1-40", "黑球");
        put("1-41", "绿光");
        put("1-42", "法师塔是什么？");
        put("1-43", "你叫什么？");
        put("1-44", "四下看看");
        put("1-45", "这应该就是阵眼");
        put("1-46", "布鲁斯");
        put("1-47", "迷路了");
        put("1-48", "想你了");
        put("1-49", "后悔了");
        put("1-50", "预言");
        put("1-51", "有件事需要查");
        put("1-52", "去找奥利");
        put("1-53", "看看成品箭");
        put("1-54", "进去等他");
        put("1-55", "为了出名");
        put("1-56", "为了生存");
        put("1-57", "因为我想");
        put("1-58", "过去坐在篝火边");
        put("1-59", "野外点火");
        put("1-60", "胆小鬼");
        put("1-61", "有点可爱");
        put("1-62", "把树枝捡回去");
        put("1-63", "事态快速发展");
        put("1-64", "把他捆上");
        put("1-65", "去百羽镇看看");
        put("1-66", "继续前进");
        put("1-67", "你与失踪有关吗");
        put("1-68", "邀请他一起上路");
        put("1-69", "人在哪儿");
        put("1-70", "你为什么要抓人");
        put("1-71", "你究竟是什么人");
        put("1-72", "答应");
        put("1-73", "第二步");
        put("1-74", "第三步");
        put("1-75", "完成");
        put("1-76", "很不错");
        put("1-77", "凑合");
        put("1-78", "还有下次");
        put("1-79", "下次是什么时候");
        put("1-80", "我怎么联系你");
        put("1-81", "再聊聊");
        put("1-82", "答应");
        put("2-1", "银鳞村");
        put("2-2", "百羽镇");
        put("2-3", "天使城");
        put("2-4", "魔法知识");
        put("2-5", "传说记载");
        put("2-6", "大陆历史");
        put("2-7", "昨天迷路的原因");
        put("2-8", "跟着奥利");
        put("2-9", "在镇上走走");
        put("2-10", "问黑暗力量");
        put("2-11", "四处逛逛");
        put("2-12", "你家里的箭");
        put("2-13", "躲开");
        put("2-14", "不动");
        put("2-15", "您以前见过它");
        put("2-16", "道谢离开");
        put("2-17", "自然之力？");
        put("2-18", "你是果子？");
        put("2-19", "你知道精灵吗？");
        put("2-20", "告辞");
        put("2-21", "有别的怪事吗？");
        put("2-22", "你都知道什么？");
        put("2-23", "不问了");
        put("2-24", "进神殿");
        put("2-25", "进神殿");
        put("2-26", "我也不知道");
        put("2-27", "石台之下");
        put("2-28", "问翡翠剑的事");
        put("2-29", "那你知道什么");
        put("2-30", "那谁会知道");
        put("2-31", "他还活着？");
        put("2-32", "这不是废话吗");
        put("2-33", "我听我听");
        put("3-1", "龙骨雪山");
        put("3-2", "龙骨雪山");
        put("3-3", "龙骨雪山");
        put("3-4", "接受传送");
        put("3-5", "爬");
        put("3-6", "谁在那儿");
        put("3-7", "摸剑");
        put("3-8", "观察他");
        put("3-9", "拍他一下");
        put("3-10", "继续观察");
        put("3-11", "寻找其他线索");
        put("3-12", "别人的记忆");
        put("3-13", "你做的梦");
        put("3-14", "瑟尔");
        put("3-15", "翡翠剑");
        put("3-16", "深入凹痕");
        put("3-17", "找藤蔓");
        put("3-18", "继续前进");
        put("3-19", "瑟尔？");
        put("3-20", "阿宾？");
        put("3-21", "阿琳？");
        put("3-22", "你认得瑟尔？");
        put("3-23", "坦诚相告");
        put("3-24", "我还要脸");
        put("3-25", "他是我的敌人？");
        put("3-26", "他还可以被拯救吗？");
        put("3-27", "如实告知");
        put("3-28", "含糊过去");
        put("3-29", "请说");
        put("3-30", "不爬");
        put("3-31", "去看看");
        put("3-32", "怎么选这儿");
        put("3-33", "这里安全吗");
        put("3-34", "可以参观吗");
        put("3-35", "处理材料");
        put("3-36", "怎么处理");
        put("3-37", "什么属性");
        put("3-38", "去找卡萝");
        put("3-39", "去找卡萝");
        put("3-40", "黑暗领域怎么走");
        put("3-41", "专心赶路");
        put("3-42", "拿上");
        put("3-43", "继续上路");
        put("3-44", "进去看看");
        put("3-45", "继续上路");
        put("3-46", "爬上去看看");
        put("3-47", "爬上去看看");
        put("3-48", "爬上去看看");
        put("3-49", "有什么能帮忙的");
        put("3-50", "先祭奠一下");
        put("3-51", "直接动手挖坟");
        put("3-52", "回溯");
        put("3-53", "头骨");
        put("3-54", "胸骨");
        put("3-55", "臂骨");
        put("3-56", "脊椎");
        put("3-57", "破烂披风");
        put("3-58", "下一步计划");
        put("3-59", "讨伐魔王");
        put("3-60", "去哥谭");
        put("3-61", "去哥谭");
        put("3-62", "向左");
        put("3-63", "向右");
        put("3-64", "山林");
        put("3-65", "向右");
        put("3-66", "向上游");
        put("3-67", "左转");
        put("3-68", "出去看看");
        put("3-69", "好好休息");
        put("3-70", "布鲁斯？");
        put("3-71", "防御");
        put("3-72", "进攻");
        put("3-73", "你怎么在这儿");
        put("3-74", "鹰魔是什么");
        put("3-75", "需要帮忙吗");
        put("3-76", "坚持帮忙");
        put("3-77", "不再插手");
        put("3-78", "等雪停");
        put("3-79", "稍后跟上");
        put("3-80", "立刻跟上");
        put("3-81", "在山洞等");
        put("4-1", "黑暗领域");
        put("4-2", "黑暗领域");
        put("4-3", "下山");
        put("4-4", "衣着肮脏的强壮武士");
        put("4-5", "职业均衡的守卫小队");
        put("4-6", "带着兜帽的孤身法师");
        put("4-7", "拒绝");
        put("4-8", "你到底是什么人");
        put("4-9", "你在小镇干什么");
        put("4-10", "你怎么会在这儿");
        put("4-11", "我可以相信你吗");
        put("4-12", "战斗");
        put("4-13", "战斗");
        put("4-14", "你哪位");
        put("4-15", "有什么事");
        put("4-16", "你又要我上你吗");
        put("4-17", "这里不安全");
        put("4-18", "脱衣服");
        put("4-19", "你真奇怪");
        put("4-20", "成吧");
        put("4-21", "怎么问这个");
        put("4-22", "我在考虑");
        put("4-23", "答应");
        put("4-24", "拒绝");
        put("4-25", "出发");
        put("4-26", "出发");
        put("4-27", "不请我进你家看看吗？");
        put("4-28", "拔剑");
        put("4-29", "没错");
        put("5-1", "哥谭");
        put("5-2", "继续前进");
        put("5-3", "继续前进");
        put("5-4", "哥谭");
        put("5-5", "中央广场");
        put("5-6", "中央广场");
        put("5-7", "中央广场");
        put("5-8", "你找我有什么事");
        put("5-9", "布鲁斯？");
        put("5-10", "布鲁斯？");
        put("5-11", "是你？");
        put("5-12", "你好");
        put("5-13", "你到底是什么人？");
        put("5-14", "你找我来干什么？");
        put("5-15", "什么？");
        put("5-16", "一楼（客厅）");
        put("5-17", "再逛逛");
        put("5-18", "二楼（客房）");
        put("5-19", "三楼（主卧）");
        put("5-20", "下层（厨房）");
        put("5-21", "上层（天台）");
        put("5-22", "下层（书房）");
        put("5-23", "上层（收藏）");
        put("5-24", "地下室");
        put("5-25", "地下室");
        put("5-26", "继续前进");
        put("5-27", "继续前进");
        put("5-28", "休息");
        put("5-29", "要他解释");
        put("5-30", "要他解释");
        put("5-31", "半信半疑");
        put("5-32", "帮忙找出卧底");
        put("5-33", "北边城堡");
        put("5-34", "拿上提灯");
        put("5-35", "拿上生命晶石");
        put("5-36", "找布鲁斯");
        put("5-37", "带回去");
        put("5-38", "能救活吗？");
        put("5-39", "能救活吗？");
        put("5-40", "中央广场");
        put("5-41", "中央广场");
        put("5-42", "追上去");
        put("5-43", "追上去");
        put("5-44", "城东枯井");
        put("5-45", "爬下去");
        put("5-46", "城南旧屋");
        put("5-47", "城南旧屋");
        put("5-48", "准备陷阱");
        put("5-49", "准备作战");
        put("5-50", "不做准备");
        put("5-51", "包括龙蛋吗？");
        put("5-52", "带回去给布鲁斯");
        put("5-53", "接下来做什么");
        put("5-54", "我知道了");
        put("5-55", "当天晚上");
        put("5-56", "回房睡觉");
        put("5-57", "跟着他走");
        put("5-58", "跟着他走");
        put("5-59", "东塔楼");
        put("5-60", "地下室");
        put("5-61", "地下室");
        put("5-62", "摸一下");
        put("5-63", "先回城堡");
        put("5-64", "准备偷袭");
        put("6-1", "决战之日");
        put("6-2", "布鲁斯");
        put("6-3", "哥谭百姓");
        put("6-4", "光明骑士团");
        put("6-5", "魔王");
        put("7-1", "进城逛逛");
        put("7-2", "继续听");
        put("7-3", "继续听");
        put("7-4", "你跑调了");
        put("7-5", "不就是个悲剧");
        put("7-6", "那个故事真的发生了");
        put("7-7", "先查查布鲁斯是谁");
        put("7-8", "你是什么人");
        put("7-9", "你是天使？");
        put("end-1", "无事发生");
        put("end-2", "出师未捷");
        put("end-3", "宁死不屈");
        put("end-4", "牡丹花下");
        put("end-5", "笼中之鸟");
        put("end-6", "不自量力");
        put("end-7", "无心之过");
        put("end-8", "不见天日");
        put("end-9", "命丧他乡");
        put("end-10", "翡翠暮光");
        put("end-11", "家养猫咪");
        put("end-12", "晴空万里");
        put("end-13", "匹夫之勇");
        put("end-14", "猎魔人");
        put("end-15", "万灵恸哭");
        put("end-16", "旭日东升");
        put("end-17", "无尽冒险");
        put("end-18", "翡翠长明");
        put("end-19", "视差未来");
        put("end-20", "未曾设想");
        put("end-21", "破晓曙光");
    }};

    static HashMap<String, Integer> default_para() {
        return new HashMap<String, Integer>() {{
            put(BRUCE_STORY_LINE, 0);
            put(BRUCE_SHOW_UP, 0);
            put(BRUCE_LOVE, 0);
            put(BRUCE_INTRODUCE, 0);
            put(OLIVER_STORY_LINE, 0);
            put(OLIVER_LOVE, 0);
            put(SINESTRO_STORY_LINE, 0);
            put(SINESTRO_LOVE, 0);
            put(SINESTRO_TAME, 0);
            put(BARRY_LOVE, 0);

            put(TEAMMATE, 0);
            put(SWORD_HOT_TIME, 0);
            put(KNOWLEDGE, 0);
            put(INTELLIGENCE, 0);
            put(TEMPORARY, 0);
            put(PROPS, 0);
            put(PEGASUS, 0);
            put(DRAGON_EGG, 0);
        }};
    }

    static int getSceneTextId(String scene) {
        int tmp = 0;
        switch (scene) {
            case "1-1":
                tmp = R.string.s1_1;
                break;
            case "1-10":
                tmp = R.string.s1_10;
                break;
            case "1-11":
                tmp = R.string.s1_11;
                break;
            case "1-12":
                tmp = R.string.s1_12;
                break;
            case "1-13":
                tmp = R.string.s1_13;
                break;
            case "1-14":
                tmp = R.string.s1_14;
                break;
            case "1-15":
                tmp = R.string.s1_15;
                break;
            case "1-16":
                tmp = R.string.s1_16;
                break;
            case "1-17":
                tmp = R.string.s1_17;
                break;
            case "1-18":
                tmp = R.string.s1_18;
                break;
            case "1-19":
                tmp = R.string.s1_19;
                break;
            case "1-2":
                tmp = R.string.s1_2;
                break;
            case "1-20":
                tmp = R.string.s1_20;
                break;
            case "1-21":
                tmp = R.string.s1_21;
                break;
            case "1-22":
                tmp = R.string.s1_22;
                break;
            case "1-23":
                tmp = R.string.s1_23;
                break;
            case "1-24":
                tmp = R.string.s1_24;
                break;
            case "1-25":
                tmp = R.string.s1_25;
                break;
            case "1-26":
                tmp = R.string.s1_26;
                break;
            case "1-27":
                tmp = R.string.s1_27;
                break;
            case "1-28":
                tmp = R.string.s1_28;
                break;
            case "1-29":
                tmp = R.string.s1_29;
                break;
            case "1-3":
                tmp = R.string.s1_3;
                break;
            case "1-30":
                tmp = R.string.s1_30;
                break;
            case "1-31":
                tmp = R.string.s1_31;
                break;
            case "1-32":
                tmp = R.string.s1_32;
                break;
            case "1-33":
                tmp = R.string.s1_33;
                break;
            case "1-34":
                tmp = R.string.s1_34;
                break;
            case "1-35":
                tmp = R.string.s1_35;
                break;
            case "1-36":
                tmp = R.string.s1_36;
                break;
            case "1-37":
                tmp = R.string.s1_37;
                break;
            case "1-38":
                tmp = R.string.s1_38;
                break;
            case "1-39":
                tmp = R.string.s1_39;
                break;
            case "1-4":
                tmp = R.string.s1_4;
                break;
            case "1-40":
                tmp = R.string.s1_40;
                break;
            case "1-41":
                tmp = R.string.s1_41;
                break;
            case "1-42":
                tmp = R.string.s1_42;
                break;
            case "1-43":
                tmp = R.string.s1_43;
                break;
            case "1-44":
                tmp = R.string.s1_44;
                break;
            case "1-45":
                tmp = R.string.s1_45;
                break;
            case "1-46":
                tmp = R.string.s1_46;
                break;
            case "1-47":
                tmp = R.string.s1_47;
                break;
            case "1-48":
                tmp = R.string.s1_48;
                break;
            case "1-49":
                tmp = R.string.s1_49;
                break;
            case "1-5":
                tmp = R.string.s1_5;
                break;
            case "1-50":
                tmp = R.string.s1_50;
                break;
            case "1-51":
                tmp = R.string.s1_51;
                break;
            case "1-52":
                tmp = R.string.s1_52;
                break;
            case "1-53":
                tmp = R.string.s1_53;
                break;
            case "1-54":
                tmp = R.string.s1_54;
                break;
            case "1-55":
                tmp = R.string.s1_55;
                break;
            case "1-56":
                tmp = R.string.s1_56;
                break;
            case "1-57":
                tmp = R.string.s1_57;
                break;
            case "1-58":
                tmp = R.string.s1_58;
                break;
            case "1-59":
                tmp = R.string.s1_59;
                break;
            case "1-6":
                tmp = R.string.s1_6;
                break;
            case "1-60":
                tmp = R.string.s1_60;
                break;
            case "1-61":
                tmp = R.string.s1_61;
                break;
            case "1-62":
                tmp = R.string.s1_62;
                break;
            case "1-63":
                tmp = R.string.s1_63;
                break;
            case "1-64":
                tmp = R.string.s1_64;
                break;
            case "1-65":
                tmp = R.string.s1_65;
                break;
            case "1-66":
                tmp = R.string.s1_66;
                break;
            case "1-67":
                tmp = R.string.s1_67;
                break;
            case "1-68":
                tmp = R.string.s1_68;
                break;
            case "1-69":
                tmp = R.string.s1_69;
                break;
            case "1-7":
                tmp = R.string.s1_7;
                break;
            case "1-70":
                tmp = R.string.s1_70;
                break;
            case "1-71":
                tmp = R.string.s1_71;
                break;
            case "1-72":
                tmp = R.string.s1_72;
                break;
            case "1-73":
                tmp = R.string.s1_73;
                break;
            case "1-74":
                tmp = R.string.s1_74;
                break;
            case "1-75":
                tmp = R.string.s1_75;
                break;
            case "1-76":
                tmp = R.string.s1_76;
                break;
            case "1-77":
                tmp = R.string.s1_77;
                break;
            case "1-78":
                tmp = R.string.s1_78;
                break;
            case "1-79":
                tmp = R.string.s1_79;
                break;
            case "1-8":
                tmp = R.string.s1_8;
                break;
            case "1-80":
                tmp = R.string.s1_80;
                break;
            case "1-81":
                tmp = R.string.s1_81;
                break;
            case "1-9":
                tmp = R.string.s1_9;
                break;
            case "2-1":
                tmp = R.string.s2_1;
                break;
            case "2-10":
                tmp = R.string.s2_10;
                break;
            case "2-11":
                tmp = R.string.s2_11;
                break;
            case "2-12":
                tmp = R.string.s2_12;
                break;
            case "2-13":
                tmp = R.string.s2_13;
                break;
            case "2-14":
                tmp = R.string.s2_14;
                break;
            case "2-15":
                tmp = R.string.s2_15;
                break;
            case "2-16":
                tmp = R.string.s2_16;
                break;
            case "2-17":
                tmp = R.string.s2_17;
                break;
            case "2-18":
                tmp = R.string.s2_18;
                break;
            case "2-19":
                tmp = R.string.s2_19;
                break;
            case "2-2":
                tmp = R.string.s2_2;
                break;
            case "2-20":
                tmp = R.string.s2_20;
                break;
            case "2-21":
                tmp = R.string.s2_21;
                break;
            case "2-22":
                tmp = R.string.s2_22;
                break;
            case "2-23":
                tmp = R.string.s2_23;
                break;
            case "2-24":
                tmp = R.string.s2_24;
                break;
            case "2-25":
                tmp = R.string.s2_25;
                break;
            case "2-26":
                tmp = R.string.s2_26;
                break;
            case "2-27":
                tmp = R.string.s2_27;
                break;
            case "2-28":
                tmp = R.string.s2_28;
                break;
            case "2-29":
                tmp = R.string.s2_29;
                break;
            case "2-3":
                tmp = R.string.s2_3;
                break;
            case "2-30":
                tmp = R.string.s2_30;
                break;
            case "2-31":
                tmp = R.string.s2_31;
                break;
            case "2-32":
                tmp = R.string.s2_32;
                break;
            case "2-33":
                tmp = R.string.s2_33;
                break;
            case "2-4":
                tmp = R.string.s2_4;
                break;
            case "2-5":
                tmp = R.string.s2_5;
                break;
            case "2-6":
                tmp = R.string.s2_6;
                break;
            case "2-7":
                tmp = R.string.s2_7;
                break;
            case "2-8":
                tmp = R.string.s2_8;
                break;
            case "2-9":
                tmp = R.string.s2_9;
                break;
            case "3-1":
                tmp = R.string.s3_1;
                break;
            case "3-10":
                tmp = R.string.s3_10;
                break;
            case "3-11":
                tmp = R.string.s3_11;
                break;
            case "3-12":
                tmp = R.string.s3_12;
                break;
            case "3-13":
                tmp = R.string.s3_13;
                break;
            case "3-14":
                tmp = R.string.s3_14;
                break;
            case "3-15":
                tmp = R.string.s3_15;
                break;
            case "3-16":
                tmp = R.string.s3_16;
                break;
            case "3-17":
                tmp = R.string.s3_17;
                break;
            case "3-18":
                tmp = R.string.s3_18;
                break;
            case "3-19":
                tmp = R.string.s3_19;
                break;
            case "3-2":
                tmp = R.string.s3_2;
                break;
            case "3-20":
                tmp = R.string.s3_20;
                break;
            case "3-21":
                tmp = R.string.s3_21;
                break;
            case "3-22":
                tmp = R.string.s3_22;
                break;
            case "3-23":
                tmp = R.string.s3_23;
                break;
            case "3-24":
                tmp = R.string.s3_24;
                break;
            case "3-25":
                tmp = R.string.s3_25;
                break;
            case "3-26":
                tmp = R.string.s3_26;
                break;
            case "3-27":
                tmp = R.string.s3_27;
                break;
            case "3-28":
                tmp = R.string.s3_28;
                break;
            case "3-29":
                tmp = R.string.s3_29;
                break;
            case "3-3":
                tmp = R.string.s3_3;
                break;
            case "3-30":
                tmp = R.string.s3_30;
                break;
            case "3-31":
                tmp = R.string.s3_31;
                break;
            case "3-32":
                tmp = R.string.s3_32;
                break;
            case "3-33":
                tmp = R.string.s3_33;
                break;
            case "3-34":
                tmp = R.string.s3_34;
                break;
            case "3-35":
                tmp = R.string.s3_35;
                break;
            case "3-36":
                tmp = R.string.s3_36;
                break;
            case "3-37":
                tmp = R.string.s3_37;
                break;
            case "3-38":
                tmp = R.string.s3_38;
                break;
            case "3-39":
                tmp = R.string.s3_39;
                break;
            case "3-4":
                tmp = R.string.s3_4;
                break;
            case "3-40":
                tmp = R.string.s3_40;
                break;
            case "3-41":
                tmp = R.string.s3_41;
                break;
            case "3-42":
                tmp = R.string.s3_42;
                break;
            case "3-43":
                tmp = R.string.s3_43;
                break;
            case "3-44":
                tmp = R.string.s3_44;
                break;
            case "3-45":
                tmp = R.string.s3_45;
                break;
            case "3-46":
                tmp = R.string.s3_46;
                break;
            case "3-47":
                tmp = R.string.s3_47;
                break;
            case "3-48":
                tmp = R.string.s3_48;
                break;
            case "3-49":
                tmp = R.string.s3_49;
                break;
            case "3-5":
                tmp = R.string.s3_5;
                break;
            case "3-50":
                tmp = R.string.s3_50;
                break;
            case "3-51":
                tmp = R.string.s3_51;
                break;
            case "3-52":
                tmp = R.string.s3_52;
                break;
            case "3-53":
                tmp = R.string.s3_53;
                break;
            case "3-54":
                tmp = R.string.s3_54;
                break;
            case "3-55":
                tmp = R.string.s3_55;
                break;
            case "3-56":
                tmp = R.string.s3_56;
                break;
            case "3-57":
                tmp = R.string.s3_57;
                break;
            case "3-58":
                tmp = R.string.s3_58;
                break;
            case "3-59":
                tmp = R.string.s3_59;
                break;
            case "3-6":
                tmp = R.string.s3_6;
                break;
            case "3-60":
                tmp = R.string.s3_60;
                break;
            case "3-61":
                tmp = R.string.s3_61;
                break;
            case "3-62":
                tmp = R.string.s3_62;
                break;
            case "3-63":
                tmp = R.string.s3_63;
                break;
            case "3-64":
                tmp = R.string.s3_64;
                break;
            case "3-65":
                tmp = R.string.s3_65;
                break;
            case "3-66":
                tmp = R.string.s3_66;
                break;
            case "3-67":
                tmp = R.string.s3_67;
                break;
            case "3-68":
                tmp = R.string.s3_68;
                break;
            case "3-69":
                tmp = R.string.s3_69;
                break;
            case "3-7":
                tmp = R.string.s3_7;
                break;
            case "3-70":
                tmp = R.string.s3_70;
                break;
            case "3-71":
                tmp = R.string.s3_71;
                break;
            case "3-72":
                tmp = R.string.s3_72;
                break;
            case "3-73":
                tmp = R.string.s3_73;
                break;
            case "3-74":
                tmp = R.string.s3_74;
                break;
            case "3-75":
                tmp = R.string.s3_75;
                break;
            case "3-76":
                tmp = R.string.s3_76;
                break;
            case "3-77":
                tmp = R.string.s3_77;
                break;
            case "3-78":
                tmp = R.string.s3_78;
                break;
            case "3-79":
                tmp = R.string.s3_79;
                break;
            case "3-8":
                tmp = R.string.s3_8;
                break;
            case "3-80":
                tmp = R.string.s3_80;
                break;
            case "3-81":
                tmp = R.string.s3_81;
                break;
            case "3-9":
                tmp = R.string.s3_9;
                break;
            case "4-1":
                tmp = R.string.s4_1;
                break;
            case "4-10":
                tmp = R.string.s4_10;
                break;
            case "4-11":
                tmp = R.string.s4_11;
                break;
            case "4-12":
                tmp = R.string.s4_12;
                break;
            case "4-13":
                tmp = R.string.s4_13;
                break;
            case "4-14":
                tmp = R.string.s4_14;
                break;
            case "4-15":
                tmp = R.string.s4_15;
                break;
            case "4-16":
                tmp = R.string.s4_16;
                break;
            case "4-17":
                tmp = R.string.s4_17;
                break;
            case "4-18":
                tmp = R.string.s4_18;
                break;
            case "4-19":
                tmp = R.string.s4_19;
                break;
            case "4-2":
                tmp = R.string.s4_2;
                break;
            case "4-20":
                tmp = R.string.s4_20;
                break;
            case "4-21":
                tmp = R.string.s4_21;
                break;
            case "4-22":
                tmp = R.string.s4_22;
                break;
            case "4-23":
                tmp = R.string.s4_23;
                break;
            case "4-24":
                tmp = R.string.s4_24;
                break;
            case "4-25":
                tmp = R.string.s4_25;
                break;
            case "4-26":
                tmp = R.string.s4_26;
                break;
            case "4-27":
                tmp = R.string.s4_27;
                break;
            case "4-28":
                tmp = R.string.s4_28;
                break;
            case "4-29":
                tmp = R.string.s4_29;
                break;
            case "4-3":
                tmp = R.string.s4_3;
                break;
            case "4-4":
                tmp = R.string.s4_4;
                break;
            case "4-5":
                tmp = R.string.s4_5;
                break;
            case "4-6":
                tmp = R.string.s4_6;
                break;
            case "4-7":
                tmp = R.string.s4_7;
                break;
            case "4-8":
                tmp = R.string.s4_8;
                break;
            case "4-9":
                tmp = R.string.s4_9;
                break;
            case "5-1":
                tmp = R.string.s5_1;
                break;
            case "5-10":
                tmp = R.string.s5_10;
                break;
            case "5-11":
                tmp = R.string.s5_11;
                break;
            case "5-12":
                tmp = R.string.s5_12;
                break;
            case "5-13":
                tmp = R.string.s5_13;
                break;
            case "5-14":
                tmp = R.string.s5_14;
                break;
            case "5-15":
                tmp = R.string.s5_15;
                break;
            case "5-16":
                tmp = R.string.s5_16;
                break;
            case "5-17":
                tmp = R.string.s5_17;
                break;
            case "5-18":
                tmp = R.string.s5_18;
                break;
            case "5-19":
                tmp = R.string.s5_19;
                break;
            case "5-2":
                tmp = R.string.s5_2;
                break;
            case "5-20":
                tmp = R.string.s5_20;
                break;
            case "5-21":
                tmp = R.string.s5_21;
                break;
            case "5-22":
                tmp = R.string.s5_22;
                break;
            case "5-23":
                tmp = R.string.s5_23;
                break;
            case "5-24":
                tmp = R.string.s5_24;
                break;
            case "5-25":
                tmp = R.string.s5_25;
                break;
            case "5-26":
                tmp = R.string.s5_26;
                break;
            case "5-27":
                tmp = R.string.s5_27;
                break;
            case "5-28":
                tmp = R.string.s5_28;
                break;
            case "5-29":
                tmp = R.string.s5_29;
                break;
            case "5-3":
                tmp = R.string.s5_3;
                break;
            case "5-30":
                tmp = R.string.s5_30;
                break;
            case "5-31":
                tmp = R.string.s5_31;
                break;
            case "5-32":
                tmp = R.string.s5_32;
                break;
            case "5-33":
                tmp = R.string.s5_33;
                break;
            case "5-34":
                tmp = R.string.s5_34;
                break;
            case "5-35":
                tmp = R.string.s5_35;
                break;
            case "5-36":
                tmp = R.string.s5_36;
                break;
            case "5-37":
                tmp = R.string.s5_37;
                break;
            case "5-38":
                tmp = R.string.s5_38;
                break;
            case "5-39":
                tmp = R.string.s5_39;
                break;
            case "5-4":
                tmp = R.string.s5_4;
                break;
            case "5-40":
                tmp = R.string.s5_40;
                break;
            case "5-41":
                tmp = R.string.s5_41;
                break;
            case "5-42":
                tmp = R.string.s5_42;
                break;
            case "5-43":
                tmp = R.string.s5_43;
                break;
            case "5-44":
                tmp = R.string.s5_44;
                break;
            case "5-45":
                tmp = R.string.s5_45;
                break;
            case "5-46":
                tmp = R.string.s5_46;
                break;
            case "5-47":
                tmp = R.string.s5_47;
                break;
            case "5-48":
                tmp = R.string.s5_48;
                break;
            case "5-49":
                tmp = R.string.s5_49;
                break;
            case "5-5":
                tmp = R.string.s5_5;
                break;
            case "5-50":
                tmp = R.string.s5_50;
                break;
            case "5-51":
                tmp = R.string.s5_51;
                break;
            case "5-52":
                tmp = R.string.s5_52;
                break;
            case "5-53":
                tmp = R.string.s5_53;
                break;
            case "5-54":
                tmp = R.string.s5_54;
                break;
            case "5-55":
                tmp = R.string.s5_55;
                break;
            case "5-56":
                tmp = R.string.s5_56;
                break;
            case "5-57":
                tmp = R.string.s5_57;
                break;
            case "5-58":
                tmp = R.string.s5_58;
                break;
            case "5-59":
                tmp = R.string.s5_59;
                break;
            case "5-6":
                tmp = R.string.s5_6;
                break;
            case "5-60":
                tmp = R.string.s5_60;
                break;
            case "5-61":
                tmp = R.string.s5_61;
                break;
            case "5-62":
                tmp = R.string.s5_62;
                break;
            case "5-63":
                tmp = R.string.s5_63;
                break;
            case "5-64":
                tmp = R.string.s5_64;
                break;
            case "5-7":
                tmp = R.string.s5_7;
                break;
            case "5-8":
                tmp = R.string.s5_8;
                break;
            case "5-9":
                tmp = R.string.s5_9;
                break;
            case "6-1":
                tmp = R.string.s6_1;
                break;
            case "6-2":
                tmp = R.string.s6_2;
                break;
            case "6-3":
                tmp = R.string.s6_3;
                break;
            case "6-4":
                tmp = R.string.s6_4;
                break;
            case "6-5":
                tmp = R.string.s6_5;
                break;
            case "7-1":
                tmp = R.string.s7_1;
                break;
            case "7-2":
                tmp = R.string.s7_2;
                break;
            case "7-3":
                tmp = R.string.s7_3;
                break;
            case "7-4":
                tmp = R.string.s7_4;
                break;
            case "7-5":
                tmp = R.string.s7_5;
                break;
            case "7-6":
                tmp = R.string.s7_6;
                break;
            case "7-7":
                tmp = R.string.s7_7;
                break;
            case "7-8":
                tmp = R.string.s7_8;
                break;
            case "7-9":
                tmp = R.string.s7_9;
                break;
            case "end-1":
                tmp = R.string.end_1;
                break;
            case "end-10":
                tmp = R.string.end_10;
                break;
            case "end-11":
                tmp = R.string.end_11;
                break;
            case "end-12":
                tmp = R.string.end_12;
                break;
            case "end-13":
                tmp = R.string.end_13;
                break;
            case "end-14":
                tmp = R.string.end_14;
                break;
            case "end-15":
                tmp = R.string.end_15;
                break;
            case "end-16":
                tmp = R.string.end_16;
                break;
            case "end-17":
                tmp = R.string.end_17;
                break;
            case "end-18":
                tmp = R.string.end_18;
                break;
            case "end-19":
                tmp = R.string.end_19;
                break;
            case "end-2":
                tmp = R.string.end_2;
                break;
            case "end-20":
                tmp = R.string.end_20;
                break;
            case "end-21":
                tmp = R.string.end_21;
                break;
            case "end-3":
                tmp = R.string.end_3;
                break;
            case "end-4":
                tmp = R.string.end_4;
                break;
            case "end-5":
                tmp = R.string.end_5;
                break;
            case "end-6":
                tmp = R.string.end_6;
                break;
            case "end-7":
                tmp = R.string.end_7;
                break;
            case "end-8":
                tmp = R.string.end_8;
                break;
            case "end-9":
                tmp = R.string.end_9;
                break;


        }
        return tmp;
    }

    static Kernel kernel = null;

    static abstract_scene getScene(String scene) {
        abstract_scene tmp = null;
        switch (scene) {
            case "1-1":
                tmp = new s1_1();
                break;
            case "1-2":
                tmp = new s1_2();
                break;
            case "1-3":
                tmp = new s1_3();
                break;
            case "1-4":
                tmp = new s1_4();
                break;
            case "1-5":
                tmp = new s1_5();
                break;
            case "1-6":
                tmp = new s1_6();
                break;
            case "1-7":
                tmp = new s1_7();
                break;
            case "1-8":
                tmp = new s1_8();
                break;
            case "1-11":
                tmp = new s1_11();
                break;
            case "1-12":
                tmp = new s1_12();
                break;
            case "1-14":
                tmp = new s1_14();
                break;
            case "1-16":
                tmp = new s1_16();
                break;
            case "1-17":
                tmp = new s1_17();
                break;
            case "1-19":
                tmp = new s1_19();
                break;
            case "1-24":
                tmp = new s1_24();
                break;
            case "1-29":
                tmp = new s1_29();
                break;
            case "1-30":
                tmp = new s1_39();
                break;
            case "1-31":
                tmp = new s1_31();
                break;
            case "1-34":
                tmp = new s1_34();
                break;
            case "1-35":
                tmp = new s1_35();
                break;
            case "1-36":
                tmp = new s1_36();
                break;
            case "1-37":
                tmp = new s1_37();
                break;
            case "1-39":
                tmp = new s1_39();
                break;
            case "1-40":
                tmp = new s1_40();
                break;
            case "1-41":
                tmp = new s1_41();
                break;
            case "1-44":
                tmp = new s1_31();
                break;
            case "1-46":
                tmp = new s1_46();
                break;
            case "1-49":
                tmp = new s1_49();
                break;
            case "1-52":
                tmp = new s1_52();
                break;
            case "1-58":
                tmp = new s1_58();
                break;
            case "1-62":
                tmp = new s1_62();
                break;
            case "1-63":
                tmp = new s1_63();
                break;
            case "1-64":
                tmp = new s1_64();
                break;
            case "1-66":
                tmp = new s1_66();
                break;
            case "1-67":
                tmp = new s1_67();
                break;
            case "1-69":
                tmp = new s1_69();
                break;
            case "1-70":
                tmp = new s1_70();
                break;
            case "1-72":
                tmp = new s1_72();
                break;
            case "1-73":
                tmp = new s1_73();
                break;
            case "1-74":
                tmp = new s1_74();
                break;
            case "1-75":
                tmp = new s1_75();
                break;
            case "1-76":
                tmp = new s1_76();
                break;
            case "2-1":
                tmp = new s2_1();
                break;
            case "2-2":
                tmp = new s2_2();
                break;
            case "2-3":
                tmp = new s2_3();
                break;
            case "2-4":
                tmp = new s2_1();
                break;
            case "2-5":
                tmp = new s2_1();
                break;
            case "2-6":
                tmp = new s2_1();
                break;
            case "2-7":
                tmp = new s2_7();
                break;
            case "2-8":
                tmp = new s2_8();
                break;
            case "2-9":
                tmp = new s2_9();
                break;
            case "2-10":
                tmp = new s2_10();
                break;
            case "2-11":
                tmp = new s2_11();
                break;
            case "2-12":
                tmp = new s2_8();
                break;
            case "2-14":
                tmp = new s2_14();
                break;
            case "2-17":
                tmp = new s2_11();
                break;
            case "2-18":
                tmp = new s2_11();
                break;
            case "2-19":
                tmp = new s2_9();
                break;
            case "2-20":
                tmp = new s2_20();
                break;
            case "2-24":
                tmp = new s2_24();
                break;
            case "2-28":
                tmp = new s2_28();
                break;
            case "2-30":
                tmp = new s2_30();
                break;
            case "3-1":
                tmp = new s3_1();
                break;
            case "3-2":
                tmp = new s3_2();
                break;
            case "3-4":
                tmp = new s3_4();
                break;
            case "3-5":
                tmp = new s3_5();
                break;
            case "3-6":
                tmp = new s3_6();
                break;
            case "3-8":
                tmp = new s3_8();
                break;
            case "3-10":
                tmp = new s3_10();
                break;
            case "3-12":
                tmp = new s3_12();
                break;
            case "3-16":
                tmp = new s3_16();
                break;
            case "3-18":
                tmp = new s3_18();
                break;
            case "3-19":
                tmp = new s3_19();
                break;
            case "3-20":
                tmp = new s3_20();
                break;
            case "3-21":
                tmp = new s3_21();
                break;
            case "3-22":
                tmp = new s3_22();
                break;
            case "3-23":
                tmp = new s3_23();
                break;
            case "3-31":
                tmp = new s3_31();
                break;
            case "3-32":
                tmp = new s3_31();
                break;
            case "3-33":
                tmp = new s3_31();
                break;
            case "3-34":
                tmp = new s3_31();
                break;
            case "3-35":
                tmp = new s3_35();
                break;
            case "3-36":
                tmp = new s3_36();
                break;
            case "3-37":
                tmp = new s3_37();
                break;
            case "3-41":
                tmp = new s3_41();
                break;
            case "3-43":
                tmp = new s3_43();
                break;
            case "3-45":
                tmp = new s3_45();
                break;
            case "3-46":
                tmp = new s3_46();
                break;
            case "3-52":
                tmp = new s3_52();
                break;
            case "3-53":
                tmp = new s3_52();
                break;
            case "3-54":
                tmp = new s3_52();
                break;
            case "3-55":
                tmp = new s3_52();
                break;
            case "3-56":
                tmp = new s3_52();
                break;
            case "3-57":
                tmp = new s3_52();
                break;
            case "3-58":
                tmp = new s3_58();
                break;
            case "3-59":
                tmp = new s3_59();
                break;
            case "3-60":
                tmp = new s3_60();
                break;
            case "3-61":
                tmp = new s3_61();
                break;
            case "3-62":
                tmp = new s3_62();
                break;
            case "3-65":
                tmp = new s3_65();
                break;
            case "3-66":
                tmp = new s3_66();
                break;
            case "3-68":
                tmp = new s3_68();
                break;
            case "3-73":
                tmp = new s3_73();
                break;
            case "3-75":
                tmp = new s3_75();
                break;
            case "3-78":
                tmp = new s3_78();
                break;
            case "4-3":
                tmp = new s4_3();
                break;
            case "4-4":
                tmp = new s4_4();
                break;
            case "4-6":
                tmp = new s4_6();
                break;
            case "4-7":
                tmp = new s4_7();
                break;
            case "4-8":
                tmp = new s4_6();
                break;
            case "4-9":
                tmp = new s4_6();
                break;
            case "4-10":
                tmp = new s4_6();
                break;
            case "4-11":
                tmp = new s4_11();
                break;
            case "4-13":
                tmp = new s4_13();
                break;
            case "4-14":
                tmp = new s4_14();
                break;
            case "4-15":
                tmp = new s4_14();
                break;
            case "4-16":
                tmp = new s4_14();
                break;
            case "4-20":
                tmp = new s4_20();
                break;
            case "4-21":
                tmp = new s4_21();
                break;
            case "4-25":
                tmp = new s4_25();
                break;
            case "4-26":
                tmp = new s4_25();
                break;
            case "4-27":
                tmp = new s4_27();
                break;
            case "4-28":
                tmp = new s4_28();
                break;
            case "5-1":
                tmp = new s5_1();
                break;
            case "5-2":
                tmp = new s5_2();
                break;
            case "5-4":
                tmp = new s5_4();
                break;
            case "5-10":
                tmp = new s5_10();
                break;
            case "5-15":
                tmp = new s5_15();
                break;
            case "5-17":
                tmp = new s5_15();
                break;
            case "5-18":
                tmp = new s5_18();
                break;
            case "5-28":
                tmp = new s5_28();
                break;
            case "5-29":
                tmp = new s5_29();
                break;
            case "5-30":
                tmp = new s5_29();
                break;
            case "5-32":
                tmp = new s5_32();
                break;
            case "5-33":
                tmp = new s5_33();
                break;
            case "5-34":
                tmp = new s5_32();
                break;
            case "5-35":
                tmp = new s5_32();
                break;
            case "5-36":
                tmp = new s5_32();
                break;
            case "5-37":
                tmp = new s5_37();
                break;
            case "5-40":
                tmp = new s5_32();
                break;
            case "5-41":
                tmp = new s5_41();
                break;
            case "5-44":
                tmp = new s5_44();
                break;
            case "5-45":
                tmp = new s5_32();
                break;
            case "5-46":
                tmp = new s5_32();
                break;
            case "5-47":
                tmp = new s5_47();
                break;
            case "5-51":
                tmp = new s5_32();
                break;
            case "5-53":
                tmp = new s5_53();
                break;
            case "5-55":
                tmp = new s5_55();
                break;
            case "5-57":
                tmp = new s5_57();
                break;
            case "5-58":
                tmp = new s5_58();
                break;
            case "5-63":
                tmp = new s5_33();
                break;
            case "7-1":
                tmp = new s7_1();
                break;
            case "7-2":
                tmp = new s7_2();
                break;
            case "7-3":
                tmp = new s7_3();
                break;
            case "7-5":
                tmp = new s7_5();
                break;
            case "7-6":
                tmp = new s7_6();
                break;

        }
        return tmp;
    }

    static abstract_choice getSingleChoice(String scene) {
        abstract_choice tmp = null;
        switch (scene) {
            case "1-9":
                tmp = new c1_4_3();
                break;
            case "1-10":
                tmp = new c1_4_3();
                break;
            case "1-13":
                tmp = new c1_5_1();
                break;
            case "1-15":
                tmp = new c1_15_1();
                break;
            case "1-18":
                tmp = new c1_6_1();
                break;
            case "1-20":
                tmp = new c1_12_0();
                break;
            case "1-21":
                tmp = new c1_12_0();
                break;
            case "1-22":
                tmp = new c1_12_0();
                break;
            case "1-23":
                tmp = new c1_12_0();
                break;
            case "1-25":
                tmp = new c1_24_0();
                break;
            case "1-26":
                tmp = new c1_24_0();
                break;
            case "1-27":
                tmp = new c1_24_0();
                break;
            case "1-28":
                tmp = new c1_24_0();
                break;
            case "1-32":
                tmp = new c1_31_2();
                break;
            case "1-33":
                tmp = new c1_16_1();
                break;
            case "1-38":
                tmp = new c1_38_1();
                break;
            case "1-42":
                tmp = new c1_41_2();
                break;
            case "1-43":
                tmp = new c1_16_3();
                break;
            case "1-45":
                tmp = new c1_31_2();
                break;
            case "1-47":
                tmp = new c1_16_1();
                break;
            case "1-48":
                tmp = new c1_14_1();
                break;
            case "1-50":
                tmp = new c1_16_3();
                break;
            case "1-51":
                tmp = new c1_16_2();
                break;
            case "1-53":
                tmp = new c1_52_2();
                break;
            case "1-54":
                tmp = new c1_16_2();
                break;
            case "1-55":
                tmp = new c1_11_4();
                break;
            case "1-56":
                tmp = new c1_11_4();
                break;
            case "1-57":
                tmp = new c1_11_4();
                break;
            case "1-59":
                tmp = new c1_58_4();
                break;
            case "1-60":
                tmp = new c1_58_4();
                break;
            case "1-61":
                tmp = new c1_58_4();
                break;
            case "1-65":
                tmp = new c1_64_2();
                break;
            case "1-68":
                tmp = new c1_67_3();
                break;
            case "1-71":
                tmp = new c1_71_1();
                break;
            case "1-77":
                tmp = new c1_16_2();
                break;
            case "1-78":
                tmp = new c1_76_4();
                break;
            case "1-79":
                tmp = new c1_76_4();
                break;
            case "1-80":
                tmp = new c1_76_4();
                break;
            case "1-81":
                tmp = new c1_81_1();
                break;
            case "2-13":
                tmp = new c2_10_2();
                break;
            case "2-15":
                tmp = new c2_15_1();
                break;
            case "2-16":
                tmp = new c2_16_1();
                break;
            case "2-21":
                tmp = new c2_9_1();
                break;
            case "2-22":
                tmp = new c2_20_2();
                break;
            case "2-23":
                tmp = new c2_7_1();
                break;
            case "2-25":
                tmp = new c2_25_1();
                break;
            case "2-26":
                tmp = new c2_25_1();
                break;
            case "2-27":
                tmp = new c2_25_1();
                break;
            case "2-29":
                tmp = new c2_28_2();
                break;
            case "2-31":
                tmp = new c2_31_1();
                break;
            case "2-32":
                tmp = new c2_30_1();
                break;
            case "2-33":
                tmp = new c2_14_1();
                break;
            case "3-3":
                tmp = new c3_3_1();
                break;
            case "3-7":
                tmp = new c3_5_1();
                break;
            case "3-9":
                tmp = new c3_6_1();
                break;
            case "3-11":
                tmp = new c3_8_1();
                break;
            case "3-13":
                tmp = new c3_14_1();
                break;
            case "3-14":
                tmp = new c3_14_1();
                break;
            case "3-15":
                tmp = new c3_14_1();
                break;
            case "3-17":
                tmp = new c3_17_1();
                break;
            case "3-24":
                tmp = new c3_24_1();
                break;
            case "3-25":
                tmp = new c3_28_1();
                break;
            case "3-26":
                tmp = new c3_28_1();
                break;
            case "3-27":
                tmp = new c3_27_1();
                break;
            case "3-28":
                tmp = new c3_28_1();
                break;
            case "3-29":
                tmp = new c3_29_1();
                break;
            case "3-30":
                tmp = new c3_30_1();
                break;
            case "3-38":
                tmp = new c3_38_1();
                break;
            case "3-39":
                tmp = new c3_38_1();
                break;
            case "3-40":
                tmp = new c3_40_1();
                break;
            case "3-42":
                tmp = new c3_42_1();
                break;
            case "3-44":
                tmp = new c3_44_1();
                break;
            case "3-47":
                tmp = new c3_46_2();
                break;
            case "3-48":
                tmp = new c3_48_1();
                break;
            case "3-49":
                tmp = new c3_49_1();
                break;
            case "3-50":
                tmp = new c3_4_3();
                break;
            case "3-51":
                tmp = new c3_4_3();
                break;
            case "3-63":
                tmp = new c3_63_1();
                break;
            case "3-64":
                tmp = new c3_64_1();
                break;
            case "3-67":
                tmp = new c3_67_1();
                break;
            case "3-69":
                tmp = new c3_69_1();
                break;
            case "3-70":
                tmp = new c3_68_4();
                break;
            case "3-71":
                tmp = new c3_68_4();
                break;
            case "3-72":
                tmp = new c3_68_4();
                break;
            case "3-74":
                tmp = new c3_73_2();
                break;
            case "3-76":
                tmp = new c3_75_4();
                break;
            case "3-77":
                tmp = new c3_75_4();
                break;
            case "3-79":
                tmp = new c3_78_4();
                break;
            case "3-80":
                tmp = new c3_78_4();
                break;
            case "3-81":
                tmp = new c3_78_4();
                break;
            case "4-1":
                tmp = new c4_1_1();
                break;
            case "4-2":
                tmp = new c4_1_1();
                break;
            case "4-5":
                tmp = new c4_5_1();
                break;
            case "4-12":
                tmp = new c4_12_1();
                break;
            case "4-17":
                tmp = new c4_14_4();
                break;
            case "4-18":
                tmp = new c4_14_4();
                break;
            case "4-19":
                tmp = new c4_14_4();
                break;
            case "4-22":
                tmp = new c4_22_1();
                break;
            case "4-23":
                tmp = new c4_23_1();
                break;
            case "4-24":
                tmp = new c4_23_2();
                break;
            case "4-29":
                tmp = new c4_22_1();
                break;
            case "5-3":
                tmp = new c5_3_1();
                break;
            case "5-5":
                tmp = new c5_2_4();
                break;
            case "5-6":
                tmp = new c5_2_4();
                break;
            case "5-7":
                tmp = new c5_2_4();
                break;
            case "5-8":
                tmp = new c5_8_1();
                break;
            case "5-9":
                tmp = new c5_4_3();
                break;
            case "5-11":
                tmp = new c5_4_3();
                break;
            case "5-12":
                tmp = new c5_3_1();
                break;
            case "5-13":
                tmp = new c5_13_1();
                break;
            case "5-14":
                tmp = new c5_14_1();
                break;
            case "5-16":
                tmp = new c5_16_1();
                break;
            case "5-19":
                tmp = new c5_16_1();
                break;
            case "5-20":
                tmp = new c5_16_1();
                break;
            case "5-21":
                tmp = new c5_16_1();
                break;
            case "5-22":
                tmp = new c5_16_1();
                break;
            case "5-23":
                tmp = new c5_16_1();
                break;
            case "5-24":
                tmp = new c5_16_1();
                break;
            case "5-25":
                tmp = new c5_16_1();
                break;
            case "5-26":
                tmp = new c5_1_2();
                break;
            case "5-27":
                tmp = new c5_8_1();
                break;
            case "5-31":
                tmp = new c5_31_1();
                break;
            case "5-38":
                tmp = new c5_38_1();
                break;
            case "5-39":
                tmp = new c5_52_1();
                break;
            case "5-42":
                tmp = new c5_38_1();
                break;
            case "5-43":
                tmp = new c5_38_1();
                break;
            case "5-48":
                tmp = new c5_48_1();
                break;
            case "5-49":
                tmp = new c5_49_1();
                break;
            case "5-50":
                tmp = new c5_38_1();
                break;
            case "5-52":
                tmp = new c5_52_1();
                break;
            case "5-54":
                tmp = new c5_53_2();
                break;
            case "5-56":
                tmp = new c5_59_1();
                break;
            case "5-59":
                tmp = new c5_59_1();
                break;
            case "5-60":
                tmp = new c5_60_1();
                break;
            case "5-61":
                tmp = new c5_60_1();
                break;
            case "5-62":
                tmp = new c5_59_1();
                break;
            case "5-64":
                tmp = new c5_49_1();
                break;
            case "6-1":
                tmp = new c6_1_1();
                break;
            case "6-2":
                tmp = new c6_2_1();
                break;
            case "6-3":
                tmp = new c6_3_1();
                break;
            case "6-4":
                tmp = new c6_4_1();
                break;
            case "6-5":
                tmp = new c6_5_1();
                break;
            case "7-4":
                tmp = new c7_3_2();
                break;
            case "7-7":
                tmp = new c7_8_1();
                break;
            case "7-8":
                tmp = new c7_8_1();
                break;
            case "7-9":
                tmp = new c7_8_1();
                break;
        }
        return tmp;
    }

    static LinkedList<abstract_choice> getChoices(String scene) {
        if (scene.contains("end")) {
            return new LinkedList<abstract_choice>() {{
                add(new choice_end(scene));
            }};
        } else if (kernel.getPosition() != 0) {
            if (kernel.getPosition() == 1) {
                return new s5_15_1().load();
            } else if (kernel.getPosition() == 2) {
                return new s5_15_2().load();
            } else {
                return new s5_15_3().load();
            }
        } else {
            abstract_choice c = getSingleChoice(scene);
            if (c != null) {
                return new LinkedList<abstract_choice>() {{
                    add(c);
                }};
            } else {
                abstract_scene s = getScene(scene);
                return s.load();
            }
        }
    }

    static String getTitle(String s) {
        if (s.startsWith("1")) {
            return "第一章 出发";
        } else if (s.startsWith("2")) {
            return "第二章 传说";
        } else if (s.startsWith("3")) {
            return "第三章 雪山";
        } else if (s.startsWith("4")) {
            return "第四章 远方";
        } else if (s.startsWith("5")) {
            return "第五章 危城";
        } else if (s.startsWith("6")) {
            return "第六章 孤光";
        } else if (s.startsWith("7")) {
            return "外传 黎明";
        } else {
            return "结局";
        }
    }
}
