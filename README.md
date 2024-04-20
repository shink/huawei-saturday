# 华为月末周六 iOS 日历订阅

<p align="center">
    <a href="https://github.com/shink/huawei-saturday/actions/workflows/submit-pr.yml"><img src="https://github.com/shink/huawei-saturday/actions/workflows/submit-pr.yml/badge.svg" /></a>
    <img src="https://img.shields.io/badge/language-python-3572A5.svg" />
    <img src="https://img.shields.io/github/stars/shink/huawei-saturday.svg?label=stars&logo=github" />
    <img src="https://img.shields.io/github/forks/shink/huawei-saturday.svg?label=forks&logo=github" />
</p>

## Usage

根据 [config/sat.yml](config/sat.yml) 配置文件，由 GitHub Actions 自动生成日历内容并提交 pull request，如: [pull#20](https://github.com/shink/huawei-saturday/pull/20)

配置文件格式如下：

```yaml
year: 2024
months:
    - 1
    - 3
    - 5
    - 6
    - 7
    - 8
    - 10
    - 12
days:
    - 01-01
    - 11-01
    - 12-31
```

订阅地址：

- https://raw.githubusercontent.com/shink/huawei-saturday/master/calendar.ics

> [!CAUTION]
>
> **为避免导致信息安全问题，请勿在订阅时将“账户”选择为 iCloud**！
>
> 账户：
>  - iCloud
>  - 我的 iPhone ✔

## License

[GPL V3 License](LICENSE)
