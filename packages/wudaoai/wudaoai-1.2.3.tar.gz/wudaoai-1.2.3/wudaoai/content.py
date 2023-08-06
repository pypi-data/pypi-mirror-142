import json
import requests

# 测试or生产 域名

url_pre = "https://open.wudaoai.com/api/"

# 短key转token
def get_token(key):
    url = url_pre + "paas/passApiToken/getToken/" + key
    page = requests.get(url)
    page = page.content
    page = page.decode('utf-8')
    token = json.loads(page)
    return token

# 模型接口
def send(engine, key, context,
        temperature=1,
        topP=0,
        generatedLength=128,
        topK=3,
        presencePenalty=1,
        frequencyPenalty=1,
        repetitionPenalty=1.2,
        noRepeatNgramSize=3,
        num_title=3
         ):


    # 模型选择
    if engine == "question_answer":
        url = url_pre + "paas/model/v1/open/engines/question_answer/txl-general-engine-v1"
        params = {
            "inputText": context["prompt"],
            "inputTextDesc": context["promptDesc"],
            "temperature": temperature,
            "topP": topP,
            "generatedLength": generatedLength,
            "topK": topK,
            "abilityType": "qa",
            "presencePenalty": presencePenalty,
            "frequencyPenalty": frequencyPenalty
        }
    elif engine == "content_creation":
        url = url_pre + "paas/model/v1/open/engines/content_creation/text-general-engine-v1"
        params = {
            "inputText": context["prompt"],
            "temperature": temperature,
            "topP": topP,
            "generatedLength": generatedLength,
            "topK": topK,
            "presencePenalty": presencePenalty,
            "frequencyPenalty": frequencyPenalty
        }
    elif engine == "chat":
        url = url_pre + "paas/model/v1/open/engines/chat/chat-general-engine-v1"
        params = {
            "inputText": context["prompt"],
            "temperature": temperature,
            "topP": topP,
            "generatedLength": generatedLength,
            "topK": topK,
            "repetitionPenalty": repetitionPenalty,
            "noRepeatNgramSize": noRepeatNgramSize
            }
    elif engine == "couplet_generation":
        #http: // open.wudaoai.com / stage - api / paas / model / v1 / open / engines
        url = url_pre + "paas/model/v1/open/engines/couplet_generation/txl-general-engine-v1"
        params = {
            "inputText": context["prompt"]
        }
    elif engine == "titleKey_generation":
        if num_title > 10:
            num_title = 10
        if num_title < 1:
            num_title = 1
        url = url_pre + "paas/model/v1/open/engines/titleKey_generation/text-general-engine-v1"
        params = {
            "inputText": context["prompt"],
            "numTitle": num_title
        }
    elif engine == "titleDes_generation":
        if num_title > 10:
            num_title = 10
        if num_title < 1:
            num_title = 1
        url = url_pre + "paas/model/v1/open/engines/titleDes_generation/text-general-engine-v1"
        params = {
            "inputText": context["prompt"],
            "numTitle": num_title
        }
    else:
        print("please choose the correct engine.")

    # 短key变长token,然后拿出长key
    token = get_token(key)
    if token['code'] == 200:
        key = token['data']
    else:
        print(token)
        return

    # 请求头
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": key,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    # 请求体
    response = requests.post(url, data=json.dumps(params), headers=headers)
    if response.status_code == requests.codes.ok:
        print(response.text)




