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


def parse_slide_time_content(content, current_bpm):
    """
    解析 [...] 内部内容，返回 delay, duration。
    delay 只用于整条 SLIDE 开始前等待；连锁 SLIDE 的后续分段不再重复等待。
    """
    content = content.strip()

    if not content:
        return Fraction(1), Fraction(0)

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

    return Fraction(1), parse_time_value(content, current_bpm)


def parse_slide_time(n, current_bpm):
    """
    保留原接口：从完整 SLIDE 字符串里取第一个 [...]。
    """
    if '[' not in n or ']' not in n:
        return Fraction(1), Fraction(0)

    content = n.split('[', 1)[1].split(']', 1)[0].strip()
    return parse_slide_time_content(content, current_bpm)


def parse_slide_duration_content(content, current_bpm):
    """
    只解析 duration，不解析等待时间。
    用于连锁 SLIDE 的分段时长。
    """
    content = content.strip()

    if '##' in content:
        content = content.split('##', 1)[1]

    return parse_time_value(content, current_bpm)


def scan_slide_part(part):
    """
    扫描单条 SLIDE 轨道：
    - 数字：按钮点
    - [...]：时长参数
    不使用正则，避免误读括号内数字。
    """
    cleaned = part.translate(str.maketrans('', '', 'xbf@$?!'))

    digits = []
    brackets = []

    i = 0
    while i < len(cleaned):
        ch = cleaned[i]

        if ch == '[':
            j = cleaned.find(']', i + 1)
            if j == -1:
                break

            brackets.append((i, j, cleaned[i + 1:j].strip()))
            i = j + 1
            continue

        if ch in '12345678':
            digits.append((i, int(ch) - 1))

        i += 1

    has_slide_symbol = any(ch in slide_symbols for ch in cleaned)
    return cleaned, digits, brackets, has_slide_symbol


def parse_slide_chain(part, default_start=None):
    """
    把一条 SLIDE 解析成连续分段。

    例：
    1-4q7-2[1:2]
      -> (1->4), (4->7), (7->2)

    -6[8:5] 且 default_start=1
      -> (1->6)
      用于 Multiple SLIDE 的省略起点写法。
    """
    cleaned, digits, brackets, has_slide_symbol = scan_slide_part(part)

    if not has_slide_symbol:
        return [], []

    if len(digits) >= 2:
        points = digits[:]
    elif len(digits) == 1 and default_start is not None:
        points = [(-1, default_start), digits[0]]
    else:
        return [], []

    buttons = [k for _, k in points]
    segments = list(zip(buttons, buttons[1:]))

    # 找每个分段终点后面有没有自己的 [...]
    seg_brackets = []

    for seg_i in range(len(segments)):
        after_pos = points[seg_i + 1][0]
        before_pos = points[seg_i + 2][0] if seg_i + 2 < len(points) else len(cleaned) + 1

        content = None

        for b_start, b_end, b_content in brackets:
            if after_pos < b_start < before_pos:
                content = b_content
                break

        seg_brackets.append(content)

    return segments, seg_brackets


def split_duration_by_x_distance(segments, total_duration):
    """
    没有逐段写时长时，把总时长分配给各段。

    注意：你的 RPE 输出只用 positionX 模拟 slide，
    所以这里按 X 距离近似分配；不还原 p/q/s/z/V/w 的真实几何轨迹长度。
    """
    if total_duration <= 0:
        return [Fraction(0) for _ in segments]

    weights = [
        Fraction(str(round(abs(key[end_k] - key[start_k]), 6)))
        for start_k, end_k in segments
    ]

    if not any(w > 0 for w in weights):
        weights = [Fraction(1) for _ in segments]

    total_weight = sum(weights, Fraction(0))

    durations = []
    used = Fraction(0)

    for w in weights[:-1]:
        d = total_duration * w / total_weight
        durations.append(d)
        used += d

    durations.append(total_duration - used)
    return durations


def make_slide_segment_points(segment_start_time, start_k, end_k, duration, include_start=True):
    """
    生成单个分段的 drag 点。
    """
    notes = []

    if duration <= 0:
        notes.append(drag(segment_start_time, start_k))
        return notes

    t = Fraction(0)

    # 连锁第二段以后不要重复插入连接点
    if not include_start:
        t += SLIDE_STEP

    while t < duration:
        ratio = t / duration

        x = key[start_k] + (key[end_k] - key[start_k]) * float(ratio)

        d = drag(segment_start_time + t, start_k)
        d['positionX'] = x
        notes.append(d)

        t += SLIDE_STEP

    d = drag(segment_start_time + duration, end_k)
    d['positionX'] = key[end_k]
    notes.append(d)

    return notes


def make_slide_chain_drag_points(startTime, segments, seg_brackets, current_bpm):
    """
    生成一条 SLIDE 轨道的 drag 点。
    支持：
    1-4q7-2[1:2]
    1-4[2:1]q7[2:1]-2[1:1]
    """
    if not segments:
        return []

    # 每段都有自己的 [...]：使用逐段时长
    if all(c is not None for c in seg_brackets):
        delay, _ = parse_slide_time_content(seg_brackets[0], current_bpm)
        durations = [
            parse_slide_duration_content(c, current_bpm)
            for c in seg_brackets
        ]

    # 只有最后一个 [...]：作为整条连锁 SLIDE 的总时长
    else:
        final_content = next((c for c in reversed(seg_brackets) if c is not None), None)

        if final_content is None:
            delay, total_duration = Fraction(1), Fraction(0)
        else:
            delay, total_duration = parse_slide_time_content(final_content, current_bpm)

        durations = split_duration_by_x_distance(segments, total_duration)

    notes = []
    cursor = startTime + delay

    for i, ((start_k, end_k), duration) in enumerate(zip(segments, durations)):
        notes.extend(
            make_slide_segment_points(
                cursor,
                start_k,
                end_k,
                duration,
                include_start=(i == 0)
            )
        )
        cursor += duration

    return notes


def simulate_slide(startTime, n, current_bpm):
    """
    支持：
    - 普通 SLIDE：1-5[8:1]
    - Multiple SLIDE：1-4[4:3]*-6[8:5]
    - 连锁 SLIDE：1-4q7-2[1:2]
    - 连锁逐段时长：1-4[2:1]q7[2:1]-2[1:1]
    """
    notes = []

    cleaned_whole = n.translate(str.maketrans('', '', 'xbf@$'))

    first_digit = None
    for ch in cleaned_whole:
        if ch in '12345678':
            first_digit = int(ch) - 1
            break

    # simai 的 ? / ! 是无星星 SLIDE
    no_star_tap = '?' in n or '!' in n

    if first_digit is not None and not no_star_tap:
        notes.append(tap(startTime, first_digit))

    # * 是 Multiple SLIDE：每条轨道都从原始起点开始，不是从上一条终点开始
    parts = n.split('*')
    root_start = first_digit

    for part in parts:
        part = part.strip()
        if not part:
            continue

        segments, seg_brackets = parse_slide_chain(part, root_start)

        if not segments:
            continue

        notes.extend(
            make_slide_chain_drag_points(
                startTime,
                segments,
                seg_brackets,
                current_bpm
            )
        )

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
                raw_n = n.strip()
                n = raw_n.translate(str.maketrans('', '', 'xbf@$?'))
                if n.isdigit(): outChart['judgeLineList'][0]['notes'].append(tap(time,int(n)-1))
                elif 'h' in n:
                    holdTime = n.split('[')[1].split(']')[0].split(':')
                    n = n.translate(str.maketrans('', '', 'ABCDE'))
                    outChart['judgeLineList'][0]['notes'].append(hold(time,time + Fraction(int(holdTime[1]) * 4, int(holdTime[0])),int(n[0])-1))
                elif n and n[0] in 'ABCDE':
                    n = n.translate(str.maketrans('', '', 'ABCDE'))
                    outChart['judgeLineList'][0]['notes'].append(drag(time,int(n[0])-1))
                elif any(c in raw_n for c in slide_symbols):
                    outChart['judgeLineList'][0]['notes'].extend(
                        simulate_slide(time, raw_n, current_bpm)
                    )
            time += Fraction(4, div)
outChart['judgeLineList'][0]['numOfNotes'] = len(outChart['judgeLineList'][0]['notes'])
with open('chart.json','w') as f: dump(outChart,f)