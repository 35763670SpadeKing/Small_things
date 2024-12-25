import requests
import pandas as pd
import time
import base64
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 通过秘钥获取Basic Authorization值
def generate_basic_auth(client_id, client_secret):
    """
    生成 Basic Authorization 字符串
    :param client_id: 客户端ID
    :param client_secret: 客户端密钥
    :return: Base64编码后的认证字符串
    """
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return encoded_credentials

# 通过Basic Authorization获取token
def get_token(client_id, client_secret, token_url):
    # 生成Basic Authorization
    basic_auth = generate_basic_auth(client_id, client_secret)
    
    # 设置请求头
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {basic_auth}'
    }
    
    # 设置请求体
    data = {
        'grant_type': 'client_credentials'
    }
    
    try:
        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()  # 检查请求是否成功
        token = response.json().get('access_token')  # 从响应中获取token
        return token
    except requests.exceptions.RequestException as e:
        logging.error(f"获取token失败: {e}")
        return None

# 单独的请求处理函数
def process_request(api_url, headers, data):
    """
    处理单个请求
    :param api_url: API接口请求地址
    :param headers: 请求头，包含token
    :param data: 请求参数
    :return: 请求参数、响应数据、请求耗时（秒）
    """
    try:
        start_time = time.time()
        response = requests.post(api_url, params=data, headers=headers)
        response.raise_for_status()  # 如果请求失败，抛出异常

        elapsed_time = time.time() - start_time
        return data, response.json(), elapsed_time
    except requests.exceptions.RequestException as e:
        logging.error(f"请求失败: {e}")
        return data, {"error": str(e)}, None

# 发送API请求
def send_api_requests(api_url, token, input_file_path, output_file_path):
    # 设置请求头，包含token
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        df = pd.read_excel(input_file_path)
    except Exception as e:
        logging.error(f"读取Excel文件失败: {e}")
        return

    # 获取excel文件的第四列数据作为入参,如果需要改动请根据实际情况进行修改,数字为列索引,从0开始,所以3为第四列
    input_data = df.iloc[:, 3]

    results = []  # 用于存储请求结果
    request_times = []  # 用于存储请求耗时
    input_params = []  # 用于存储请求参数

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(process_request, api_url, headers, eval(data) if not isinstance(data, dict) else data)
            for data in input_data
        ]
        
        for future in as_completed(futures):
            input_param, response_data, elapsed_time = future.result()
            request_times.append(elapsed_time)  # 记录本次请求耗时
            results.append(response_data)  # 记录响应数据
            input_params.append(input_param)  # 记录请求参数

            # 打印请求参数和响应数据，耗时
            if elapsed_time is not None:
                logging.info(f"入参: {input_param} | 出参: {response_data} | 耗时: {elapsed_time:.2f}秒")
            else:
                logging.info(f"入参: {input_param} | 出参: {response_data}")

    # 将结果保存到result.xlsx文件
    result_df = pd.DataFrame({
        "input_param": input_params,
        "response_data": results,
        "request_time": request_times
    })
    try:
        result_df.to_excel(output_file_path, index=False)  # 保存结果到excel文件
    except Exception as e:
        logging.error(f"保存结果到Excel文件失败: {e}")

if __name__ == "__main__":
    # API接口请求地址
    api_url = ""
    # token请求地址
    token_url = ""
    # 客户端凭证
    client_id = ""
    client_secret = ""
    
    # 获取token
    token = get_token(client_id, client_secret, token_url)
    
    if token:
        # 入参文件路径，必须为xlsx格式的excel文件
        input_file_path = "C://Users/92156/Desktop/output.xlsx"
        # 输出文件路径
        output_file_path = "C://Users/92156/Desktop/1.xlsx"
        send_api_requests(api_url, token, input_file_path, output_file_path)
    else:
        logging.error("无法获取有效的token，程序终止")
