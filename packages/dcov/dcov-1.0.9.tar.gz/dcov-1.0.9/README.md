增量覆盖率工具 DCOV
===================

## 介绍

dcov 是一个 `通过 git 统计不同 branch 之间差异，并生成报告` 的工具， 它主要有以下功能:

1. 统计两个 branch 之间的差异，生成 `差异报告`

```
# dcov --compare-branch HEAD^ 
Diff changes between HEAD^ and HEAD
changed files: 11, changed lines: 185

dcov/diff_cover_tool.py (1 lines): 231
dcov/git_diff.py (1 lines): 102
dcov/report_generator.py (12 lines): 23-25, 27-28, 35, 103-105, 111, 178, 188
dcov/templates/console_coverage_report.txt (6 lines): 1-2, 4, 13, 19, 22
dcov/templates/console_quality_report.txt (5 lines): 1, 5, 17, 23, 26
dcov/templates/html_coverage_report.html (1 lines): 9
dcov/templates/markdown_coverage_report.md (7 lines): 1-3, 8, 10, 12-13
dcov/violationsreporters/violations_reporter.py (38 lines): 5, 28, 30, 32-33, 37, 68, 74-75, 77, 192-193, 218-223, 225-226, 228, 230, 232-245, 248, 251
pyproject.toml (2 lines): 3-4
README.md (73 lines): 4-76
tests/data/cobe.xml (39 lines): 1-39
```

2. 根据标准的 `cobertura` 或则 `clover` 格式的单元测试覆盖率报告，生成增量覆盖率, 下面这个例子是我用 `phpunit` 单元测试覆盖率报告 cobe.xml 生成增量覆盖率报告，可以看到工具会生成每个文件对应的覆盖率情况，以及没有覆盖的代码所在的行号

```
# dcov --compare-branch HEAD^ --coverage_xml tests/data/cobe.xml
--------------------------
Diff Coverage Report
Diff: HEAD^ HEAD, staged and unstaged changes
--------------------------
dcov/diff_cover_tool.py (0.0%): Missing lines 231
dcov/git_diff.py (0.0%): Missing lines 102
dcov/report_generator.py (0.0%): Missing lines 23-25,27-28,35,103-105,111,178,188
dcov/templates/console_coverage_report.txt (0.0%): Missing lines 1-2,4,13,19,22
dcov/templates/console_quality_report.txt (0.0%): Missing lines 1,5,17,23,26
dcov/templates/html_coverage_report.html (0.0%): Missing lines 9
dcov/templates/markdown_coverage_report.md (0.0%): Missing lines 1-3,8,10,12-13
dcov/violationsreporters/violations_reporter.py (2.6%): Missing lines 5,28,30,32-33,37,68,74,77,192-193,218-223,225-226,228,230,232-245,248,251
pyproject.toml (0.0%): Missing lines 3-4
README.md (0.0%): Missing lines 4-76
tests/data/cobe.xml (0.0%): Missing lines 1-39
--------------------------
Total:   185 lines
Missing: 184 lines
Coverage: 0%
--------------------------
```

## 前提

本工具需要系统安装 `git` 工具

## 安装

直接通过 `pip` 安装

```
pip install dcov
dcov --version
```

通过 `dcov --help` 查看常用的功能

```
# 黑白名单, 如我不想把 app/ 和 scripts/ 目录下的文件加入覆盖率计算
dcov --compare-branch @~15 --exclude */app/* */scripts/*

# 忽略空白差异
dcov --compare-branch @~15 --ignore-whitespace

# 生成覆盖率报告,支持 html json markdown 格式, 以下是生成 html 格式报告
dcov --compare-branch @~15 --coverage_xml coverage_unit_test.xml --exclude */app/* */scripts/* --html-report this_is_our_html_report.html
```

## 贡献代码

开发需要使用到 `poetry` 工具

```
pip install poetry
```

在 fork 本仓库 [dcov](https://github.com/xiak/dcov), 在您本人仓库开发后再提交 `PR` 合并回本仓库

```
git clone https://github.com/xxxxxxx/dcov.git
cd dcov
poetry run dcov --version
```

## 感谢

本工具原作者为 [Bachmann1234](https://github.com/Bachmann1234/diff_cover)

dcov 在原工具基础上加入一些新特性，以及修改了原来的覆盖率计算方法。
