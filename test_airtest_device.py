import os
import allure

from airtest.core.api import connect_device, keyevent, snapshot


DEVICE_URI = "Android://127.0.0.1:5037/emulator-5554"
SCREENSHOT_PATH = "reports/airtest_home.png"


@allure.title("Airtest Android 设备连接与截图测试")
@allure.description("验证雷电模拟器连接、屏幕信息、HOME 操作和截图功能。")
def test_android_device():

    device = None

    try:
        with allure.step("1. 连接 Android 模拟器"):
            device = connect_device(DEVICE_URI)
            assert device is not None, "设备连接失败"

            print("Device:", device.uuid)
            allure.attach(
                device.uuid,
                name="设备信息",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("2. 设置 ADBCAP 截图方式"):
            device.screen_proxy = "ADBCAP"
            print("Screenshot method:", device.screen_proxy.method_name)

        with allure.step("3. 获取设备分辨率"):
            resolution = device.get_current_resolution()
            print("Resolution:", resolution)

            assert resolution[0] > 0 and resolution[1] > 0, \
                "设备分辨率异常"

            allure.attach(
                str(resolution),
                name="设备分辨率",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("4. 执行 HOME 操作"):
            keyevent("HOME")
            print("HOME operation: PASS")

        with allure.step("5. 执行截图并添加报告附件"):
            os.makedirs("reports", exist_ok=True)

            snapshot(filename=SCREENSHOT_PATH)

            assert os.path.exists(SCREENSHOT_PATH), "截图文件不存在"

            allure.attach.file(
                SCREENSHOT_PATH,
                name="模拟器 HOME 页面截图",
                attachment_type=allure.attachment_type.PNG
            )

            print("Screenshot: PASS")

        print("TEST PASSED")

    finally:
        if device is not None:
            device.disconnect()


if __name__ == "__main__":
    test_android_device()
