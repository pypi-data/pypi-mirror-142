# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_log',
 'zdppy_log.libs',
 'zdppy_log.libs.colorama',
 'zdppy_log.libs.loguru']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zdppy-log',
    'version': '0.1.6',
    'description': 'Python中用于记录日志的工具库，简单而优美，灵活而强大',
    'long_description': '# zdppy_log\n\npython的日志库\n\n项目地址：https://github.com/zhangdapeng520/zdppy_log\n\n安装方式\n\n```shell script\npip install zdppy_log\n```\n\n使用方式\n\n```python\nfrom zdppy_log import Log\n\nlog1 = Log("logs/zdppy/zdppy_log1.log")\n\n\n@log1.catch()\ndef my_function(x, y, z):\n    # An error? It\'s caught anyway!\n    return 1 / (x + y + z)\n\n\nmy_function(0, 0, 0)\n# logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod\n\nlog2 = Log("logs/zdppy/zdppy_log2.log")\nlog2.debug("log2日志")\nlog2.info("log2日志")\nlog2.warning("log2日志")\nlog2.error("log2日志")\nlog2.critical("log2日志")\n\nlog3 = Log("logs/zdppy/zdppy_log3.log", debug=False)\nlog3.debug("log3日志")\nlog3.info("log3日志")\nlog3.warning("log3日志")\nlog3.error("log3日志")\nlog3.critical("log3日志")\n```\n\n## 版本历史\n\n- 版本0.1.2 2022年2月19日 增加debug模式；默认json日志为False\n- 版本0.1.3 2022年3月4日 增加记录日志文件，日志方法，日志行数的功能\n- 版本0.1.4 2022年3月5日 移除第三方依赖\n- 版本0.1.5 2022年3月5日 增加控制是否开启日志全路径的开关量\n- 版本0.1.6 2022年3月16日 增加只输出到控制台的开关量及底层代码优化\n',
    'author': 'zhangdapeng',
    'author_email': 'pygosuperman@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zhangdapeng520/zdppy_log',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
