import streamlit as st

st.set_page_config(page_title="톤트윈 Tone Twin", page_icon="💄", layout="centered")

# =========================================================
# 데이터 (원본 html의 BRANDS / PRODUCTS / SHADES를 그대로 이식)
# x: 웜(-5) ~ 쿨(+5), y: 딥(-5) ~ 라이트(+5)
# =========================================================
BRANDS = {
    "rainbow":   {"name": "무지개맨션", "maker": "한국콜마"},
    "atte":      {"name": "아떼", "maker": "코스맥스"},
    "tonymoly":  {"name": "토니모리", "maker": "코스맥스"},
    "peripera":  {"name": "페리페라", "maker": "코스맥스"},
    "laka":      {"name": "라카", "maker": "코스맥스"},
    "fwee":      {"name": "퓌", "maker": "씨앤씨인터내셔널"},
    "tce":       {"name": "3CE", "maker": "씨앤씨인터내셔널"},
    "naming":    {"name": "네이밍", "maker": "코스맥스"},
    "colorgram": {"name": "컬러그램", "maker": "한국콜마"},
}

PRODUCTS = {
    "rainbow_muted":     {"brand": "rainbow",   "name": "뮤티드 블러 틴트"},
    "atte_authentic":    {"brand": "atte",      "name": "어센틱 립 글로이 밤"},
    "tonymoly_shocking": {"brand": "tonymoly",  "name": "퍼펙트 립스 쇼킹 립"},
    "peripera_mood":     {"brand": "peripera",  "name": "무드 글로이 틴트"},
    "laka_twin":         {"brand": "laka",      "name": "퍼펙트 트윈 립"},
    "fwee_gloss":        {"brand": "fwee",      "name": "3D 볼류밍 글로스"},
    "tce_lazypop":       {"brand": "tce",       "name": "레이지 팝 립 스테인"},
    "naming_overdue":    {"brand": "naming",    "name": "오버 듀 글로시 립 틴트"},
    "colorgram_nudy":    {"brand": "colorgram", "name": "누디 블러 틴트"},
}

SHADES = [
    {"p": "rainbow_muted", "name": "줄리", "x": -2, "y": 4},
    {"p": "rainbow_muted", "name": "프할린", "x": -2.5, "y": 2},
    {"p": "rainbow_muted", "name": "임지", "x": -3, "y": 1},
    {"p": "rainbow_muted", "name": "플러터", "x": 0, "y": 0.5},
    {"p": "rainbow_muted", "name": "네스트", "x": -3, "y": -2},
    {"p": "rainbow_muted", "name": "베이크드", "x": -4, "y": -4},
    {"p": "rainbow_muted", "name": "디어리", "x": 2, "y": 4},
    {"p": "rainbow_muted", "name": "러비", "x": 4, "y": 3},
    {"p": "rainbow_muted", "name": "플리에", "x": 4, "y": 1},
    {"p": "rainbow_muted", "name": "모어", "x": 1, "y": -0.5},
    {"p": "rainbow_muted", "name": "파우트", "x": 1.5, "y": -1.5},
    {"p": "rainbow_muted", "name": "트레이스", "x": 4, "y": -4},

    {"p": "atte_authentic", "name": "뉴디", "x": -3, "y": 3},
    {"p": "atte_authentic", "name": "메이", "x": -4, "y": 2},
    {"p": "atte_authentic", "name": "대슬", "x": -3.5, "y": 1.5},
    {"p": "atte_authentic", "name": "베이비", "x": -0.5, "y": 2.5},
    {"p": "atte_authentic", "name": "버드", "x": 0, "y": 1.5},
    {"p": "atte_authentic", "name": "드림", "x": -0.5, "y": 0},
    {"p": "atte_authentic", "name": "소이 모브", "x": 2.5, "y": 3},
    {"p": "atte_authentic", "name": "포그", "x": 2.5, "y": 1},
    {"p": "atte_authentic", "name": "피그코어", "x": -2, "y": -1},
    {"p": "atte_authentic", "name": "크레이브", "x": -3.5, "y": -2},
    {"p": "atte_authentic", "name": "피그베일", "x": 0.5, "y": -2},
    {"p": "atte_authentic", "name": "플러트", "x": 2, "y": -3},

    {"p": "tonymoly_shocking", "code": "N19", "name": "알로하쇼킹", "x": 0.5, "y": 4},
    {"p": "tonymoly_shocking", "code": "N20", "name": "선키스쇼킹", "x": -0.5, "y": 4.3},
    {"p": "tonymoly_shocking", "code": "N13", "name": "애프리콧쇼킹", "x": -2, "y": 3.5},
    {"p": "tonymoly_shocking", "code": "N12", "name": "페어리쇼킹", "x": 3, "y": 2.5},
    {"p": "tonymoly_shocking", "code": "S04", "name": "그레이프쇼킹", "x": 2, "y": 1.5},
    {"p": "tonymoly_shocking", "code": "N04", "name": "핑크쇼킹", "x": 4.5, "y": 0.5},
    {"p": "tonymoly_shocking", "code": "N14", "name": "피치쇼킹", "x": -0.5, "y": 2.5},
    {"p": "tonymoly_shocking", "code": "S05", "name": "선셋볼쇼킹", "x": -2.5, "y": 2},
    {"p": "tonymoly_shocking", "code": "S01", "name": "오렌지쇼킹", "x": -4.5, "y": 1.5},
    {"p": "tonymoly_shocking", "code": "N03", "name": "코랄쇼킹", "x": -0.5, "y": 0.7},
    {"p": "tonymoly_shocking", "code": "N01", "name": "루비쇼킹", "x": -2, "y": 0.7},
    {"p": "tonymoly_shocking", "code": "S03", "name": "애플쇼킹", "x": 0, "y": 1},
    {"p": "tonymoly_shocking", "code": "N11", "name": "로제트쇼킹", "x": 4.5, "y": -0.3},
    {"p": "tonymoly_shocking", "code": "N02", "name": "토마토쇼킹", "x": -1.5, "y": -0.7},
    {"p": "tonymoly_shocking", "code": "N05", "name": "페탈쇼킹", "x": 3, "y": -1.5},
    {"p": "tonymoly_shocking", "code": "N10", "name": "모브쇼킹", "x": 1.5, "y": -1.7},
    {"p": "tonymoly_shocking", "code": "N08", "name": "로즈쇼킹", "x": -2, "y": -1.7},
    {"p": "tonymoly_shocking", "code": "S02", "name": "브릭쇼킹", "x": -3.5, "y": -2},
    {"p": "tonymoly_shocking", "code": "N18", "name": "베리진쇼킹", "x": 4, "y": -3},
    {"p": "tonymoly_shocking", "code": "N09", "name": "플럼쇼킹", "x": 1.5, "y": -3},
    {"p": "tonymoly_shocking", "code": "N06", "name": "레드쇼킹", "x": 0, "y": -3.5},
    {"p": "tonymoly_shocking", "code": "N07", "name": "번트로즈쇼킹", "x": -1.5, "y": -3},

    {"p": "peripera_mood", "code": "01", "name": "딸기기니", "x": -1, "y": 4},
    {"p": "peripera_mood", "code": "02", "name": "쩡신차렷", "x": -2, "y": 3.3},
    {"p": "peripera_mood", "code": "03", "name": "말랑물복", "x": -2.5, "y": 2.7},
    {"p": "peripera_mood", "code": "04", "name": "저쩔복숭아", "x": -1.5, "y": 2.7},
    {"p": "peripera_mood", "code": "05", "name": "갓기요정", "x": 1, "y": 3.3},
    {"p": "peripera_mood", "code": "06", "name": "갓기천사", "x": 2, "y": 3},
    {"p": "peripera_mood", "code": "07", "name": "자두뿜뿜", "x": -2, "y": 1.3},
    {"p": "peripera_mood", "code": "08", "name": "핑토당토", "x": -1, "y": 0.7},
    {"p": "peripera_mood", "code": "09", "name": "맘찍로즈", "x": -2.3, "y": 1},
    {"p": "peripera_mood", "code": "10", "name": "내입술인척", "x": 0, "y": 0.7},
    {"p": "peripera_mood", "code": "11", "name": "비주얼센터", "x": 1.5, "y": 1},
    {"p": "peripera_mood", "code": "12", "name": "개강아이스", "x": 2.5, "y": 0.3},
    {"p": "peripera_mood", "code": "13", "name": "분위기아씨", "x": -1.7, "y": 1.6},
    {"p": "peripera_mood", "code": "14", "name": "로지위시", "x": -0.8, "y": -1.3},
    {"p": "peripera_mood", "code": "15", "name": "맘콕로즈", "x": -2.7, "y": -1},
    {"p": "peripera_mood", "code": "16", "name": "로즈콕", "x": -0.5, "y": -2.7},
    {"p": "peripera_mood", "code": "17", "name": "이로지무화과", "x": 2, "y": -1.7},
    {"p": "peripera_mood", "code": "18", "name": "손웜수템", "x": -2, "y": 2},
    {"p": "peripera_mood", "code": "19", "name": "어쩔체리", "x": 2.7, "y": -1.7},
    {"p": "peripera_mood", "code": "20", "name": "당맛도리", "x": -3, "y": -3.3},
    {"p": "peripera_mood", "code": "21", "name": "영앤피치", "x": -3.5, "y": 2},
    {"p": "peripera_mood", "code": "22", "name": "덜익피치", "x": -2.7, "y": 2.5},
    {"p": "peripera_mood", "code": "23", "name": "맘찍피치", "x": -3.7, "y": 1.6},
    {"p": "peripera_mood", "code": "24", "name": "완익피치", "x": 0.3, "y": -0.3},
    {"p": "peripera_mood", "code": "25", "name": "포도속살", "x": 3, "y": 2},

    # 라카 차트는 세로축 위쪽 끝을 "Nude"로 표기하지만 라이트/딥과 같은 축이라 y값은 동일하게 취급
    {"p": "laka_twin", "code": "901", "name": "트루 피치", "x": 0, "y": 4.5},
    {"p": "laka_twin", "code": "902", "name": "비지 코랄", "x": -3, "y": 3.3},
    {"p": "laka_twin", "code": "903", "name": "누드 오드", "x": -1.7, "y": 2},
    {"p": "laka_twin", "code": "904", "name": "시티 핑크", "x": 2.3, "y": 2.5},
    {"p": "laka_twin", "code": "905", "name": "로지 하이", "x": 0, "y": 0},
    {"p": "laka_twin", "code": "906", "name": "올티 피그", "x": -2, "y": -2.7},
    {"p": "laka_twin", "code": "907", "name": "젠틀 로즈", "x": 1, "y": -2.3},
    {"p": "laka_twin", "code": "908", "name": "인 카페인", "x": -3.3, "y": -1.3},
    {"p": "laka_twin", "code": "909", "name": "길티 모브", "x": 2.7, "y": -1.3},
    {"p": "laka_twin", "code": "910", "name": "보스 체리", "x": 3.3, "y": -3.7},

    # 퓌 차트는 중앙 십자축이 아니라 좌하단 기준 좌표라, 차트 전체 범위를 -5~5로 정규화해서 옮겨 적음
    {"p": "fwee_gloss", "code": "01", "name": "Vanilla", "x": -2, "y": 4},
    {"p": "fwee_gloss", "code": "02", "name": "Sorbet", "x": -4.5, "y": 1.5},
    {"p": "fwee_gloss", "code": "03", "name": "Candy", "x": 2.1, "y": 3.5},
    {"p": "fwee_gloss", "code": "04", "name": "Aengdu", "x": 0.5, "y": 0.6},
    {"p": "fwee_gloss", "code": "05", "name": "Currant", "x": 3.6, "y": -2.9},
    {"p": "fwee_gloss", "code": "06", "name": "Scotch", "x": -4.4, "y": -2.4},
    {"p": "fwee_gloss", "code": "07", "name": "Peach", "x": 0.1, "y": 3.8},
    {"p": "fwee_gloss", "code": "08", "name": "Rosy", "x": -2.3, "y": 0},
    {"p": "fwee_gloss", "code": "09", "name": "Lychee", "x": -1.2, "y": 2.1},
    {"p": "fwee_gloss", "code": "10", "name": "Yogurt", "x": 4, "y": 4.8},
    {"p": "fwee_gloss", "code": "11", "name": "Taro", "x": 4, "y": -1.5},
    {"p": "fwee_gloss", "code": "13", "name": "Dirty Cola", "x": -2.8, "y": -4.4},
    {"p": "fwee_gloss", "code": "19", "name": "Vanilla Cookie", "x": -2.8, "y": -1.1},
    {"p": "fwee_gloss", "code": "20", "name": "Vanilla Sorbet", "x": 1.1, "y": -1.1},

    {"p": "tce_lazypop", "name": "베리 스프링", "x": 0.5, "y": 4},
    {"p": "tce_lazypop", "name": "에이 오어 네이", "x": -3.3, "y": 2.8},
    {"p": "tce_lazypop", "name": "캔디 플럽프", "x": 2.7, "y": 3.8},
    {"p": "tce_lazypop", "name": "쿨리스트", "x": 1, "y": 0.8},
    {"p": "tce_lazypop", "name": "뮤트 라일락", "x": 3.7, "y": 2.3},
    {"p": "tce_lazypop", "name": "로지 프로미스", "x": -0.3, "y": -0.3},
    {"p": "tce_lazypop", "name": "뮤추얼 필링", "x": -3, "y": 0.3},
    {"p": "tce_lazypop", "name": "러즈틱", "x": -2, "y": -1.3},
    {"p": "tce_lazypop", "name": "바이올렛 게이즈", "x": 3.3, "y": -1.7},
    {"p": "tce_lazypop", "name": "탠", "x": -1.7, "y": -3.7},
    {"p": "tce_lazypop", "name": "스파이스드 업", "x": 1.3, "y": -3.5},

    {"p": "naming_overdue", "name": "NUDI", "x": -1.7, "y": 4.3},
    {"p": "naming_overdue", "name": "GUANA", "x": 0.3, "y": 4.2},
    {"p": "naming_overdue", "name": "BEI", "x": 2, "y": 3.8},
    {"p": "naming_overdue", "name": "DENIA", "x": -2.7, "y": 3},
    {"p": "naming_overdue", "name": "DEWY", "x": -0.3, "y": 2.8},
    {"p": "naming_overdue", "name": "BLUSH", "x": 2.3, "y": 2.3},
    {"p": "naming_overdue", "name": "BOIL", "x": -3.3, "y": 1.7},
    {"p": "naming_overdue", "name": "NANA", "x": -1.3, "y": 1.7},
    {"p": "naming_overdue", "name": "TANZY", "x": 0.3, "y": 1.8},
    {"p": "naming_overdue", "name": "SOY", "x": 0, "y": 0.7},
    {"p": "naming_overdue", "name": "JUICY", "x": 2.3, "y": 0.7},
    {"p": "naming_overdue", "name": "SAND", "x": -4, "y": -0.3},
    {"p": "naming_overdue", "name": "ROAST", "x": 0.7, "y": -0.7},
    {"p": "naming_overdue", "name": "MAY", "x": 3, "y": -1},
    {"p": "naming_overdue", "name": "OVEDI", "x": -2.7, "y": -1.3},
    {"p": "naming_overdue", "name": "PEAK", "x": -1.3, "y": -1.3},
    {"p": "naming_overdue", "name": "HUSH", "x": 2.3, "y": -2.3},
    {"p": "naming_overdue", "name": "LORN", "x": -1, "y": -2.7},
    {"p": "naming_overdue", "name": "SIENNA", "x": 0.7, "y": -3},
    {"p": "naming_overdue", "name": "BURNT", "x": -3, "y": -3.7},
    {"p": "naming_overdue", "name": "SEPIA", "x": 2.3, "y": -3.7},

    {"p": "colorgram_nudy", "code": "01", "name": "살구살몬", "x": -3.3, "y": 4.3},
    {"p": "colorgram_nudy", "code": "15", "name": "살구라이트", "x": -2.2, "y": 4},
    {"p": "colorgram_nudy", "code": "22", "name": "잔망베이지", "x": -0.8, "y": 4.4},
    {"p": "colorgram_nudy", "code": "02", "name": "플러핑크", "x": 0.6, "y": 3.9},
    {"p": "colorgram_nudy", "code": "14", "name": "딸기벨로", "x": 2.2, "y": 4.1},
    {"p": "colorgram_nudy", "code": "32", "name": "말랑둥절", "x": -3, "y": 2.7},
    {"p": "colorgram_nudy", "code": "03", "name": "피그블리", "x": -1.8, "y": 2.8},
    {"p": "colorgram_nudy", "code": "16", "name": "로코코랄", "x": -0.8, "y": 2.3},
    {"p": "colorgram_nudy", "code": "17", "name": "이븐피치", "x": 1, "y": 2.7},
    {"p": "colorgram_nudy", "code": "24", "name": "바나누드", "x": 2.7, "y": 2.6},
    {"p": "colorgram_nudy", "code": "04", "name": "코탈릿", "x": -2.7, "y": 1.8},
    {"p": "colorgram_nudy", "code": "18", "name": "베리물리", "x": 1.2, "y": 1.8},
    {"p": "colorgram_nudy", "code": "31", "name": "말랑일락", "x": 3.3, "y": 1.1},
    {"p": "colorgram_nudy", "code": "23", "name": "잔망로즈", "x": 1.6, "y": 0.7},
    {"p": "colorgram_nudy", "code": "06", "name": "베리비키", "x": 3, "y": 0.3},
    {"p": "colorgram_nudy", "code": "08", "name": "힘초콜릿", "x": -3.7, "y": -0.6},
    {"p": "colorgram_nudy", "code": "05", "name": "레드티지", "x": -0.4, "y": -0.4},
    {"p": "colorgram_nudy", "code": "28", "name": "누디로즈", "x": -0.6, "y": -1.1},
    {"p": "colorgram_nudy", "code": "07", "name": "킥로즈", "x": 1.7, "y": -1.2},
    {"p": "colorgram_nudy", "code": "26", "name": "릭 플럼", "x": 3, "y": -1.6},
    {"p": "colorgram_nudy", "code": "11", "name": "팁초콜릿", "x": -1.7, "y": -1.8},
    {"p": "colorgram_nudy", "code": "09", "name": "바미레드", "x": -0.3, "y": -1.9},
    {"p": "colorgram_nudy", "code": "25", "name": "체리바나", "x": 2.3, "y": -2},
    {"p": "colorgram_nudy", "code": "10", "name": "데드로즈", "x": 2.7, "y": -2.7},
    {"p": "colorgram_nudy", "code": "13", "name": "번트마롱", "x": -2.7, "y": -2.8},
    {"p": "colorgram_nudy", "code": "27", "name": "브리로즈", "x": -1, "y": -2.7},
    {"p": "colorgram_nudy", "code": "29", "name": "디핑피넛", "x": -3, "y": -3.7},
    {"p": "colorgram_nudy", "code": "30", "name": "코코체리", "x": 0.7, "y": -3.8},
    {"p": "colorgram_nudy", "code": "12", "name": "플럼디헴", "x": 1.3, "y": -3.2},
]

QUICK_TRIES = [
    ("🌈 무지개맨션 · 파우트", "rainbow_muted", "파우트"),
    ("🌸 아떼 · 베이비", "atte_authentic", "베이비"),
    ("🍑 토니모리 · 코랄쇼킹", "tonymoly_shocking", "코랄쇼킹"),
    ("🍓 페리페라 · 딸기기니", "peripera_mood", "딸기기니"),
]

# =========================================================
# 색 계산 (원본 html의 hueFromX / lightnessFromY / hslToHex 이식)
# 실제 발색 hex가 아니라 좌표 기반 근사치
# =========================================================
def hue_from_x(x: float) -> float:
    h = -5 - 5 * x
    return ((h % 360) + 360) % 360


def lightness_from_y(y: float) -> float:
    return 28 + (y + 5) * ((74 - 28) / 10)


def hsl_to_hex(h: float, s: float, l: float) -> str:
    s /= 100
    l /= 100

    def k(n):
        return (n + h / 30) % 12

    a = s * min(l, 1 - l)

    def f(n):
        return l - a * max(-1, min(k(n) - 3, min(9 - k(n), 1)))

    def to_hex(v):
        return format(round(v * 255), "02x")

    return to_hex(f(0)) + to_hex(f(8)) + to_hex(f(4))


def color_for_shade(shade: dict) -> str:
    return hsl_to_hex(hue_from_x(shade["x"]), 62, lightness_from_y(shade["y"]))


def shades_for_product(product_key: str):
    return [s for s in SHADES if s["p"] == product_key]


def products_for_brand(brand_key: str):
    return {k: v for k, v in PRODUCTS.items() if v["brand"] == brand_key}


def sorted_brand_keys():
    def is_hangul(s):
        return len(s) > 0 and "\uac00" <= s[0] <= "\ud7a3"

    return sorted(BRANDS.keys(), key=lambda k: (not is_hangul(BRANDS[k]["name"]), BRANDS[k]["name"]))


def find_shade(product_key: str, color_name: str):
    for s in SHADES:
        if s["p"] == product_key and s["name"] == color_name:
            return s
    return None


# =========================================================
# 추천 로직 (원본 html의 runRecommend 이식)
# =========================================================
def run_recommend(shade: dict, own_brand: str, top_n: int = 6):
    pool = [s for s in SHADES if PRODUCTS[s["p"]]["brand"] != own_brand]
    ranked = sorted(
        pool,
        key=lambda s: ((s["x"] - shade["x"]) ** 2 + (s["y"] - shade["y"]) ** 2) ** 0.5,
    )[:top_n]
    return [(s, ((s["x"] - shade["x"]) ** 2 + (s["y"] - shade["y"]) ** 2) ** 0.5) for s in ranked]


def tier_for_distance(dist: float):
    if dist <= 1.5:
        return "매우 유사", "#FFD9E3", "#E63950"
    if dist <= 3:
        return "유사", "#F7ECEF", "#B97D8F"
    return "근접", "#F7ECEF", "#B97D8F"


# =========================================================
# 스타일 (원본 톤&매너를 최대한 재현)
# =========================================================
st.markdown(
    """
<style>
:root{
  --bg1:#FFE9EF; --bg2:#FFD3DE; --pink:#FF6F9E; --pink-deep:#FF4577;
  --red:#FF4D5E; --red-deep:#E63950; --ink:#4A2635; --muted:#B97D8F;
  --card:#FFFFFF; --line:#FFDCE6;
  --btn-pink:#E0899A; --btn-pink-dark:#D3778A;
}
.stButton button[kind="primary"]{
  background:linear-gradient(135deg, var(--btn-pink), var(--btn-pink-dark)) !important;
  border:none !important; color:#fff !important;
  box-shadow:0 8px 18px rgba(211,119,138,0.35) !important;
}
.stButton button[kind="primary"]:hover,
.stButton button[kind="primary"]:focus:not(:active){
  background:linear-gradient(135deg, var(--btn-pink-dark), var(--btn-pink)) !important;
  color:#fff !important;
  box-shadow:0 8px 18px rgba(211,119,138,0.4) !important;
}
.stButton button[kind="primary"]:active{
  background:var(--btn-pink-dark) !important; color:#fff !important;
}
.stApp{
  background:linear-gradient(160deg,var(--bg1) 0%, var(--bg2) 45%, #FFE3E8 100%);
}
h1, h2, h3{ color:var(--pink-deep) !important; text-align:center; }
.tt-brand{
  color:#FF9DC0 !important; text-align:center; font-size:42px; font-weight:800; margin-bottom:0;
  -webkit-text-stroke:1.5px #D9478A; paint-order:stroke fill;
  text-shadow:-1px -1px 0 #D9478A, 1px -1px 0 #D9478A, -1px 1px 0 #D9478A, 1px 1px 0 #D9478A;
}
.tt-brand span{ color:#FF9DC0; }
.tt-en{ text-align:center; color:var(--muted); margin-top:-8px; }
.tt-tagline{ text-align:center; color:var(--ink); line-height:1.7; margin:14px auto; max-width:380px; }
.tt-badge{
  display:block; text-align:center; margin:8px auto 0; width:fit-content;
  font-size:14.5px; color:var(--muted); background:#fff; border:1.5px dashed var(--line);
  border-radius:999px; padding:6px 16px;
}
div[data-testid="stVerticalBlockBorderWrapper"]{
  background:var(--card) !important; border-radius:24px !important; margin-top:18px;
  box-shadow:0 10px 22px rgba(255,90,130,0.12) !important; border:2px solid #fff !important;
}
div[data-testid="stVerticalBlockBorderWrapper"] h4{ color:var(--pink-deep); margin-top:0; }
.tt-chart-wrap{
  position:relative; max-width:300px; margin:22px auto 6px; padding:28px 40px;
}
.tt-chart{ position:relative; width:100%; height:220px; }
.tt-chart-hline{ position:absolute; left:0; right:0; top:50%; border-top:2px dashed var(--pink); opacity:0.55; }
.tt-chart-vline{ position:absolute; top:0; bottom:0; left:50%; border-left:2px dashed var(--pink); opacity:0.55; }
.tt-chart-dot{
  position:absolute; border-radius:50%; transform:translate(-50%,-50%);
  box-shadow:0 3px 6px rgba(0,0,0,0.10);
}
.tt-chart-axis{
  position:absolute; font-size:16px; color:var(--pink-deep); font-weight:800; white-space:nowrap;
}
.tt-chart-axis.top{ top:0; left:50%; transform:translate(-50%,-6px); }
.tt-chart-axis.bottom{ bottom:0; left:50%; transform:translate(-50%,6px); }
.tt-chart-axis.left{ left:0; top:50%; transform:translate(-6px,-50%); }
.tt-chart-axis.right{ right:0; top:50%; transform:translate(6px,-50%); }
.tt-chart-desc{ font-size:13.5px; color:var(--ink); line-height:1.8; text-align:center; margin-top:4px; }
.tt-note{
  margin-top:10px; font-size:14px; color:var(--muted); line-height:1.7;
  background:#FFF3F6; border-radius:12px; padding:9px 12px; text-align:center;
}
.tt-result-card{
  display:flex; align-items:center; gap:14px; background:#fff; border-radius:16px;
  padding:12px 16px; border:2px solid var(--line); margin-bottom:10px;
}
.tt-blob{
  width:40px; height:40px; border-radius:58% 42% 53% 47% / 55% 48% 52% 45%; flex:none;
  border:2px solid #fff; box-shadow:0 3px 8px rgba(0,0,0,0.14);
}
.tt-rinfo{ flex:1; min-width:0; }
.tt-rbrand{ font-size:12px; font-weight:700; color:var(--pink-deep); }
.tt-rname{ font-size:16px; color:var(--ink); font-weight:700; }
.tt-rproduct{ font-size:12.5px; color:var(--muted); }
.tt-why{
  flex:none; font-size:11.5px; font-weight:700; padding:6px 10px; border-radius:999px; text-align:center;
}
footer, .tt-footer{ text-align:center; font-size:12.5px; color:#D9AAB8; padding:20px 10px; line-height:1.7; }
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# 세션 상태 초기화
# =========================================================
if "brand" not in st.session_state:
    st.session_state.brand = sorted_brand_keys()[0]
if "product" not in st.session_state:
    st.session_state.product = list(products_for_brand(st.session_state.brand).keys())[0]
if "color" not in st.session_state:
    st.session_state.color = shades_for_product(st.session_state.product)[0]["name"]
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False


def apply_quick_try(product_key: str, color_name: str):
    st.session_state.brand = PRODUCTS[product_key]["brand"]
    st.session_state.product = product_key
    st.session_state.color = color_name
    st.session_state.analyzed = True


def on_brand_change():
    st.session_state.product = list(products_for_brand(st.session_state.brand).keys())[0]
    st.session_state.color = shades_for_product(st.session_state.product)[0]["name"]
    st.session_state.analyzed = False


def on_product_change():
    st.session_state.color = shades_for_product(st.session_state.product)[0]["name"]
    st.session_state.analyzed = False


# =========================================================
# 헤더
# =========================================================
st.markdown('<div class="tt-brand">💄 톤<span>트윈</span></div>', unsafe_allow_html=True)
st.markdown('<div class="tt-en">(Tone Twin)</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="tt-tagline">브랜드 컬러차트의 웜/쿨·라이트/딥 위치를 기준으로<br>'
    "가장 가까운 다른 립 제품을 찾아드려요! 💄</div>",
    unsafe_allow_html=True,
)
st.markdown('<span class="tt-badge">컬러차트 있는 브랜드 전용 · 좌표 매칭</span>', unsafe_allow_html=True)

# =========================================================
# "컬러차트"가 뭐예요? 설명 카드
# =========================================================
with st.container(border=True):
    st.markdown("#### ⏰ \"컬러차트\"가 뭐예요?")
    st.markdown(
        """
<div class="tt-chart-wrap">
  <span class="tt-chart-axis top">라이트</span>
  <span class="tt-chart-axis bottom">딥</span>
  <span class="tt-chart-axis left">웜</span>
  <span class="tt-chart-axis right">쿨</span>
  <div class="tt-chart">
    <div class="tt-chart-hline"></div>
    <div class="tt-chart-vline"></div>
    <div class="tt-chart-dot" style="left:32%;top:30%;width:28px;height:28px;background:#EFA980;"></div>
    <div class="tt-chart-dot" style="left:44%;top:40%;width:18px;height:18px;background:#D98455;"></div>
    <div class="tt-chart-dot" style="left:64%;top:26%;width:26px;height:26px;background:#F090C4;"></div>
    <div class="tt-chart-dot" style="left:76%;top:36%;width:18px;height:18px;background:#D854A0;"></div>
    <div class="tt-chart-dot" style="left:50%;top:50%;width:13px;height:13px;background:#C98CA0;"></div>
    <div class="tt-chart-dot" style="left:34%;top:62%;width:28px;height:28px;background:#9C5C46;"></div>
    <div class="tt-chart-dot" style="left:46%;top:72%;width:18px;height:18px;background:#6B3626;"></div>
    <div class="tt-chart-dot" style="left:64%;top:58%;width:26px;height:26px;background:#7C2E4C;"></div>
    <div class="tt-chart-dot" style="left:76%;top:68%;width:18px;height:18px;background:#591F38;"></div>
  </div>
</div>
<div class="tt-chart-desc">
  브랜드들이 립 제품 컬러를 <b>웜↔쿨, 라이트↔딥</b> 두 축 위에 점으로 찍어서 보여주는
  그림을 <b>"컬러차트"</b>라고 해요.<br>
  점이 가까이 있을수록 실제로도 비슷한 톤일 가능성이 높아요<br>
  — 이 앱은 그 위치를 기준으로 닮은 색을 찾아드려요!
</div>
""",
        unsafe_allow_html=True,
    )

# =========================================================
# 입력 카드
# =========================================================
with st.container(border=True):
    st.markdown("#### 💌 애정템을 골라주세요")

    brand_keys = sorted_brand_keys()
    st.selectbox(
        "브랜드",
        brand_keys,
        format_func=lambda k: BRANDS[k]["name"],
        key="brand",
        on_change=on_brand_change,
        label_visibility="collapsed",
    )

    product_options = list(products_for_brand(st.session_state.brand).keys())
    st.selectbox(
        "제품",
        product_options,
        format_func=lambda k: PRODUCTS[k]["name"],
        key="product",
        on_change=on_product_change,
        label_visibility="collapsed",
    )

    color_options = [s["name"] for s in shades_for_product(st.session_state.product)]
    st.selectbox(
        "컬러",
        color_options,
        format_func=lambda name: (
            f"#{find_shade(st.session_state.product, name)['code']} {name}"
            if find_shade(st.session_state.product, name).get("code")
            else name
        ),
        key="color",
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="tt-note">브랜드가 공개한 <b>컬러차트(웜/쿨·라이트/딥 위치)</b>가 있는 제품만 등록돼 있어요.<br>'
        "같은 위치대에 있을수록 실제로도 비슷한 톤일 가능성이 높아요!</div>",
        unsafe_allow_html=True,
    )

    if st.button("이 색이랑 닮은 색 찾아줘 ✨", use_container_width=True, type="primary"):
        st.session_state.analyzed = True

# =========================================================
# 요소3: 빠른 선택 칩
# =========================================================
st.markdown("**🙋 뭐부터 해볼지 모르겠다면, 눌러보세요!**")
chip_cols = st.columns(len(QUICK_TRIES))
for col, (label, product_key, color_name) in zip(chip_cols, QUICK_TRIES):
    with col:
        st.button(
            label,
            key=f"quick_{product_key}",
            use_container_width=True,
            on_click=apply_quick_try,
            args=(product_key, color_name),
        )

# =========================================================
# 분석 + 결과
# =========================================================
if st.session_state.analyzed:
    shade = find_shade(st.session_state.product, st.session_state.color)
    if shade is None:
        st.warning("컬러를 다시 선택해주세요.")
    else:
        product = PRODUCTS[st.session_state.product]
        brand = BRANDS[product["brand"]]
        hex_color = color_for_shade(shade)

        st.markdown("---")
        st.markdown("#### 🔍 선택하신 색")
        a1, a2 = st.columns([1, 4])
        with a1:
            st.markdown(
                f'<div class="tt-blob" style="width:56px;height:56px;background:#{hex_color};"></div>',
                unsafe_allow_html=True,
            )
        with a2:
            st.markdown(f"**{shade['name']}**")
            st.caption(f"{brand['name']} · {product['name']}")
            tone = f"{'쿨' if shade['x'] > 0 else '웜'} {abs(shade['x'])} · {'라이트' if shade['y'] > 0 else '딥'} {abs(shade['y'])}"
            st.markdown(
                f'<span class="tt-badge">{tone}</span>',
                unsafe_allow_html=True,
            )
        st.caption(
            f"컬러차트 상 웜/쿨 {shade['x']}, 라이트/딥 {shade['y']} 위치를 기준으로 가까운 색을 찾아드려요."
        )

        st.markdown("#### 💖 위치가 가까운 색은 어때요?")
        ranked = run_recommend(shade, product["brand"])
        if not ranked:
            st.info("아직 추천할 색을 못 찾았어요 🥲")
        else:
            for s, dist in ranked:
                r_product = PRODUCTS[s["p"]]
                r_brand = BRANDS[r_product["brand"]]
                r_hex = color_for_shade(s)
                tier_label, tier_bg, tier_fg = tier_for_distance(dist)
                st.markdown(
                    f"""
                    <div class="tt-result-card">
                        <div class="tt-blob" style="background:#{r_hex};"></div>
                        <div class="tt-rinfo">
                            <div class="tt-rbrand">{r_brand['name']}</div>
                            <div class="tt-rname">{s['name']}</div>
                            <div class="tt-rproduct">{r_product['name']} · {r_brand['maker']}</div>
                        </div>
                        <div class="tt-why" style="background:{tier_bg};color:{tier_fg};">
                            {tier_label}<br>(거리 {dist:.1f})
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        if st.button("다시 고르기", use_container_width=True):
            st.session_state.analyzed = False
            st.rerun()

st.markdown(
    '<div class="tt-footer">브랜드 컬러차트의 웜/쿨·라이트/딥 좌표를 기준으로 가까운 색을 추천하는 프로토타입이에요.<br>'
    "좌표는 차트를 보고 추정한 값이라 실제 발색과 차이가 있을 수 있어요 · Tone Twin Chart v0.1</div>",
    unsafe_allow_html=True,
)
