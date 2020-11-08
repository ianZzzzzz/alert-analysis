```mermaid
    graph TB
        18.log-->df-->去重-->设备id表
        df-->groupby("1-ID")-->.count-->unstack-->计算每台设备占总告警的比例-->
        衡量数据均衡程度-->推广到每个区域
        
```