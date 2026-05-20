from fractions import Fraction
from json import loads,dump
outChart = loads("""{
    "BPMList" : [],
    "META" : {
        "RPEVersion" : 160,
        "background" : "bg.png",
        "charter" : "",
        "composer" : "",
        "duration" : 0,
        "id" : "0",
        "illustration" : "",
        "level" : "0",
        "name" : "",
        "offset" : 0,
        "song" : "track.mp3"
    },
    "chartTime" : 0,
    "judgeLineGroup" : [ "Default" ],
    "judgeLineList" : [
        {
            "Group" : 0,
            "Name" : "Untitled",
            "Texture" : "line.png",
            "alphaControl" : [
                {
                    "alpha" : 1.0,
                    "easing" : 1,
                    "x" : 0.0
                },
                {
                    "alpha" : 1.0,
                    "easing" : 1,
                    "x" : 9999999.0
                }
            ],
            "anchor" : [ 0.5, 0.5 ],
            "bpmfactor" : 1.0,
            "eventLayers" : [
                {
                    "alphaEvents" : [
                        {
                            "bezier" : 0,
                            "bezierPoints" : [ 0.0, 0.0, 0.0, 0.0 ],
                            "easingLeft" : 0.0,
                            "easingRight" : 1.0,
                            "easingType" : 1,
                            "end" : 255,
                            "endTime" : [ 1, 0, 1 ],
                            "linkgroup" : 0,
                            "start" : 255,
                            "startTime" : [ 0, 0, 1 ]
                        }
                    ],
                    "moveXEvents" : [
                        {
                            "bezier" : 0,
                            "bezierPoints" : [ 0.0, 0.0, 0.0, 0.0 ],
                            "easingLeft" : 0.0,
                            "easingRight" : 1.0,
                            "easingType" : 1,
                            "end" : 0.0,
                            "endTime" : [ 1, 0, 1 ],
                            "linkgroup" : 0,
                            "start" : 0.0,
                            "startTime" : [ 0, 0, 1 ]
                        }
                    ],
                    "moveYEvents" : [
                        {
                            "bezier" : 0,
                            "bezierPoints" : [ 0.0, 0.0, 0.0, 0.0 ],
                            "easingLeft" : 0.0,
                            "easingRight" : 1.0,
                            "easingType" : 1,
                            "end" : -300.0,
                            "endTime" : [ 1, 0, 1 ],
                            "linkgroup" : 0,
                            "start" : -300.0,
                            "startTime" : [ 0, 0, 1 ]
                        }
                    ],
                    "rotateEvents" : [
                        {
                            "bezier" : 0,
                            "bezierPoints" : [ 0.0, 0.0, 0.0, 0.0 ],
                            "easingLeft" : 0.0,
                            "easingRight" : 1.0,
                            "easingType" : 1,
                            "end" : 0.0,
                            "endTime" : [ 1, 0, 1 ],
                            "linkgroup" : 0,
                            "start" : 0.0,
                            "startTime" : [ 0, 0, 1 ]
                        }
                    ],
                    "speedEvents" : [
                        {
                            "end" : 10.0,
                            "endTime" : [ 1, 0, 1 ],
                            "linkgroup" : 0,
                            "start" : 10.0,
                            "startTime" : [ 0, 0, 1 ]
                        }
                    ]
                }
            ],
            "extended" : {
                "inclineEvents" : [
                    {
                        "bezier" : 0,
                        "bezierPoints" : [ 0.0, 0.0, 0.0, 0.0 ],
                        "easingLeft" : 0.0,
                        "easingRight" : 1.0,
                        "easingType" : 0,
                        "end" : 0.0,
                        "endTime" : [ 1, 0, 1 ],
                        "linkgroup" : 0,
                        "start" : 0.0,
                        "startTime" : [ 0, 0, 1 ]
                    }
                ]
            },
            "father" : -1,
            "isCover" : 1,
            "isGif" : false,
            "notes" : [],
            "numOfNotes" : 0,
            "posControl" : [
                {
                    "easing" : 1,
                    "pos" : 1.0,
                    "x" : 0.0
                },
                {
                    "easing" : 1,
                    "pos" : 1.0,
                    "x" : 9999999.0
                }
            ],
            "sizeControl" : [
                {
                    "easing" : 1,
                    "size" : 1.0,
                    "x" : 0.0
                },
                {
                    "easing" : 1,
                    "size" : 1.0,
                    "x" : 9999999.0
                }
            ],
            "skewControl" : [
                {
                    "easing" : 1,
                    "skew" : 0.0,
                    "x" : 0.0
                },
                {
                    "easing" : 1,
                    "skew" : 0.0,
                    "x" : 9999999.0
                }
            ],
            "yControl" : [
                {
                    "easing" : 1,
                    "x" : 0.0,
                    "y" : 1.0
                },
                {
                    "easing" : 1,
                    "x" : 9999999.0,
                    "y" : 1.0
                }
            ],
            "zOrder" : 0
        }
    ],
    "multiLineString" : "0:10",
    "multiScale" : 1.0
}""")
key = [-555.88,-405.00,-238.23,-79.41,79.42,238.24,397.06,555.89]
def RPETime(t):
    return [int(t),*Fraction(t%1).limit_denominator().as_integer_ratio()]
def tap(startTime,k):
    return {
        "above" : 1,
        "alpha" : 255,
        "endTime" : RPETime(startTime),
        "isFake" : 0,
        "positionX" : key[k],
        "size" : 1.0,
        "speed" : 1.0,
        "startTime" : RPETime(startTime),
        "type" : 1,
        "visibleTime" : 999999.0,
        "yOffset" : 0.0
    }
def drag(startTime,k):
    return {
        "above" : 1,
        "alpha" : 255,
        "endTime" : RPETime(startTime),
        "isFake" : 0,
        "positionX" : key[k],
        "size" : 1.0,
        "speed" : 1.0,
        "startTime" : RPETime(startTime),
        "type" : 4,
        "visibleTime" : 999999.0,
        "yOffset" : 0.0
    }
def hold(startTime,endTime,k):
    return {
        "above" : 1,
        "alpha" : 255,
        "endTime" : RPETime(endTime),
        "isFake" : 0,
        "positionX" : key[k],
        "size" : 1.0,
        "speed" : 1.0,
        "startTime" : RPETime(startTime),
        "type" : 2,
        "visibleTime" : 999999.0,
        "yOffset" : 0.0
    }
SLIDE_STEP = Fraction(1, 16)  # 每 1/16 拍插一个 drag 点
slide_symbols = '-<>^vVwWpqsz'
current_bpm = 120


def sec_to_beat(sec, current_bpm):
    """
    秒 -> 当前 BPM 下的拍数
    """
    return Fraction(str(sec)) * Fraction(str(current_bpm)) / 60


def beat_len(value):
    """
    解析 8:3 / 16:1 这种音符长度。
    以“拍”为单位返回。
    8:3 = 4 * 3 / 8 = 1.5 拍
    """
    a, b = value.split(':', 1)
    return Fraction(int(b) * 4, int(a))


def parse_time_value(value, current_bpm):
    """
    解析右侧时间值：
    8:3        -> 当前 BPM 下的 8分音符*3
    160#8:3    -> 按 160 BPM 的 8分音符*3，再换算成当前 BPM 拍数
    1.5        -> 1.5 秒
    160#2      -> 2 秒；前面的 160# 对纯秒数没有实际影响
    """
    value = value.strip()

    if '#' in value:
        bpm_text, inner = value.split('#', 1)
        ref_bpm = Fraction(str(bpm_text))

        if ':' in inner:
            # 先算指定 BPM 下的真实秒数，再转成当前 BPM 拍数
            ref_beats = beat_len(inner)
            seconds = ref_beats * 60 / ref_bpm
            return seconds * Fraction(str(current_bpm)) / 60

        # 纯数字还是秒
        return sec_to_beat(inner, current_bpm)

    if ':' in value:
        return beat_len(value)

    # 没有 : 就是秒
    return sec_to_beat(value, current_bpm)


def parse_slide_time(n, current_bpm):
    """
    返回 delay, duration，单位都是“当前 BPM 下的拍”。

    [8:1]             -> delay=1拍, duration=8:1
    [160#8:3]         -> delay=160 BPM 下 1拍, duration=160 BPM 下 8:3
    [2]               -> delay=1拍, duration=2秒
    [160#2]           -> delay=160 BPM 下 1拍, duration=2秒
    [3##1.5]          -> delay=3秒, duration=1.5秒
    [3##8:3]          -> delay=3秒, duration=当前 BPM 下 8:3
    [3##160#8:3]      -> delay=3秒, duration=160 BPM 下 8:3
    """
    if '[' not in n or ']' not in n:
        return Fraction(1), Fraction(0)

    content = n.split('[', 1)[1].split(']', 1)[0].strip()

    if '##' in content:
        delay_text, duration_text = content.split('##', 1)
        delay = sec_to_beat(delay_text, current_bpm)
        duration = parse_time_value(duration_text, current_bpm)
        return delay, duration

    if '#' in content:
        bpm_text, value_text = content.split('#', 1)
        ref_bpm = Fraction(str(bpm_text))

        # 默认等待：指定 BPM 下的 1 拍
        delay_seconds = Fraction(60, 1) / ref_bpm
        delay = delay_seconds * Fraction(str(current_bpm)) / 60

        duration = parse_time_value(content, current_bpm)
        return delay, duration

    # 普通 [8:1] 或 [2]
    delay = Fraction(1)
    duration = parse_time_value(content, current_bpm)
    return delay, duration


def remove_bracket_content(s):
    """
    去掉 [...] 中的内容，避免把 [8:1] 里的 8 和 1 当成按钮。
    """
    out = ''
    depth = 0

    for ch in s:
        if ch == '[':
            depth += 1
            continue
        if ch == ']':
            depth = max(0, depth - 1)
            continue
        if depth == 0:
            out += ch

    return out


def find_slide_start_end(part, inherit_start=None):
    """
    找 slide 起点和终点。
    不用 re。

    例如：
    1-5[8:1]   -> 1 到 5
    6<4[16:3]  -> 6 到 4
    8w4[8:1]   -> 8 到 4
    <7[8:1]    -> 如果 inherit_start 有值，就从 inherit_start 到 7
    """
    s = remove_bracket_content(part)
    s = s.translate(str.maketrans('', '', 'xbf@$?'))

    start = None
    start_pos = -1

    for i, ch in enumerate(s):
        if ch in '12345678':
            start = int(ch) - 1
            start_pos = i
            break

    if start is None:
        start = inherit_start
        start_pos = -1

    if start is None:
        return None, None

    seen_slide_symbol = False
    end = None

    for ch in s[start_pos + 1:]:
        if ch in slide_symbols:
            seen_slide_symbol = True
            continue

        if seen_slide_symbol and ch in '12345678':
            end = int(ch) - 1

    return start, end


def make_slide_drag_points(startTime, start_k, end_k, delay, duration):
    """
    从 start_k 到 end_k 生成固定间隔 drag 点。
    """
    notes = []

    if duration <= 0:
        notes.append(drag(startTime + delay, start_k))
        return notes

    t = Fraction(0)

    while t < duration:
        ratio = t / duration

        x = key[start_k] + (key[end_k] - key[start_k]) * float(ratio)

        d = drag(startTime + delay + t, start_k)
        d['positionX'] = x
        notes.append(d)

        t += SLIDE_STEP

    # 保证终点一定有一个点
    d = drag(startTime + delay + duration, end_k)
    d['positionX'] = key[end_k]
    notes.append(d)

    return notes


def simulate_slide(startTime, n, current_bpm):
    """
    用 drag 模拟 simai slide。
    支持 * 连接的复合 slide，例如：
    8-3[8:1]*-5[8:1]
    """
    notes = []

    # slide 起点星星/起点 tap
    first_digit = None
    for ch in n:
        if ch in '12345678':
            first_digit = int(ch) - 1
            break

    if first_digit is not None:
        notes.append(tap(startTime, first_digit))

    parts = n.split('*')
    inherit_start = first_digit

    for part in parts:
        part = part.strip()
        if not part:
            continue

        start_k, end_k = find_slide_start_end(part, inherit_start)

        if start_k is None:
            continue

        if end_k is None:
            notes.append(drag(startTime, start_k))
            inherit_start = start_k
            continue

        delay, duration = parse_slide_time(part, current_bpm)

        notes.extend(
            make_slide_drag_points(startTime, start_k, end_k, delay, duration)
        )

        inherit_start = end_k

    return notes
with open('maidata.txt','r',encoding='utf-8') as f: inChart = f.read()
inChart = inChart.split('&inote_6=')[1]
time,div = 0,4
for line in inChart.split('\n'):
    if line == 'E': break
    for i,char in enumerate(line):
        if char == '(' and line[i+1:line.find(')', i+1)]:
            current_bpm = float(line[i+1:line.find(')', i+1)])

            outChart['BPMList'].append({
                'bpm': current_bpm,
                'startTime': RPETime(time)
            })
        if char == '{': div = int(line[i+1:line.find('}',i+1)])
        if char == ',':
            note = line[line.rfind(',',0,i)+1:i].split('}')[-1].split('/')
            for n in note:
                n = n.translate(str.maketrans('', '', 'xbf@$?'))
                if n.isdigit(): outChart['judgeLineList'][0]['notes'].append(tap(time,int(n)-1))
                elif 'h' in n:
                    holdTime = n.split('[')[1].split(']')[0].split(':')
                    n = n.translate(str.maketrans('', '', 'ABCDE'))
                    outChart['judgeLineList'][0]['notes'].append(hold(time,time + Fraction(int(holdTime[1]) * 4, int(holdTime[0])),int(n[0])-1))
                elif n and n[0] in 'ABCDE':
                    n = n.translate(str.maketrans('', '', 'ABCDE'))
                    outChart['judgeLineList'][0]['notes'].append(drag(time,int(n[0])-1))
                elif any(c in n for c in slide_symbols):
                    outChart['judgeLineList'][0]['notes'].extend(
                        simulate_slide(time, n, current_bpm)
                    )
            time += Fraction(4, div)
with open('chart.json','w') as f: dump(outChart,f)