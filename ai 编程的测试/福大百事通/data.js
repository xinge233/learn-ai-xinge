// 福大百事通 - 数据文件（模拟数据，仅供页面布局测试）
// 注意：后续由 Python 爬虫自动覆盖生成，你现在不用手改内容。
// 前端通过 <script src="data.js"> 引入，直接使用全局变量 FUDA_DATA。
// 用 JS 全局变量而非 .json + fetch，是为了能直接双击 index.html 打开（file:// 协议下 fetch 本地文件会被浏览器拦截）。

const FUDA_DATA = {
  updated: "2026-11-01",
  // 每条资讯的字段约定（爬虫也要按这个格式输出）：
  //   id        唯一编号（数字）
  //   category  分类（字符串，对应新闻网频道）
  //   title     标题
  //   url       原文链接（绝对地址）
  //   date      发布日期 YYYY-MM-DD
  //   summary   简短摘要（可选，爬虫可留空）
  items: [
    {
      id: 1,
      category: "福大要闻",
      title: "福州大学召开同心旗山季谈会暨党代会工作报告征求意见座谈会",
      url: "https://news.fzu.edu.cn/info/1011/126750.htm",
      date: "2026-10-31",
      summary: ""
    },
    {
      id: 2,
      category: "福大要闻",
      title: "福州大学举行首届“紫金矿业景河奖教金”颁奖典礼",
      url: "https://news.fzu.edu.cn/info/1011/126665.htm",
      date: "2026-10-27",
      summary: ""
    },
    {
      id: 3,
      category: "福大要闻",
      title: "福州大学旗山校区综合实验楼（邵武楼）举行揭牌仪式",
      url: "https://news.fzu.edu.cn/info/1011/126659.htm",
      date: "2026-10-26",
      summary: ""
    },
    {
      id: 4,
      category: "综合新闻",
      title: "福州大学迎来2026级新生",
      url: "https://news.fzu.edu.cn/info/1012/125918.htm",
      date: "2026-09-07",
      summary: ""
    },
    {
      id: 5,
      category: "综合新闻",
      title: "福建省“101”计划机械设计制造及其自动化专业教育教学改革项目启动会和研讨会在福州大学召开",
      url: "https://news.fzu.edu.cn/info/1012/126696.htm",
      date: "2026-10-27",
      summary: ""
    },
    {
      id: 6,
      category: "校园观察",
      title: "福州大学举办第二届“融春音乐节・福大乐队专场”活动",
      url: "https://news.fzu.edu.cn/info/1017/123779.htm",
      date: "2026-04-28",
      summary: ""
    }
  ]
};
