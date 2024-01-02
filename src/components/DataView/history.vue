<template>
  <div class="history-container">
    <div class="tabs"> 
      <ul class="tab-tilte">
        <li v-for="(itemTit, index) in tabTitle" :key="itemTit" @mouseover="handleMouseOver(index)" @mouseout="handleMouseOut(index)" :class="{active: cur == index}">
          {{ itemTit }}
        </li>
      </ul>
      <div class="indicatorDots">
        <span :class="{active: cur == i}" v-for="(v, i) in tabTitle" :key="i"></span>
      </div>
      <div class="tab-content">
        <div v-for="(itemCon, index) in tabCon" v-show="cur == index" :key="itemCon">
          <div v-for="(v, i) in itemCon" :key="i" class="content">
            {{ v }}
          </div>
        </div>
      </div>
    </div>   
  </div>
</template>

<script>
export default {
  name: "history",
  data() {
    return {
      timer: null,
      tabTitle: ['2014-02-13', '2014-02-14', '2014-02-15', '2014-02-16', '2014-02-17', '2014-02-18'],
      tabCon: [
        [
          '2014-02-13 06:20:00": "3.0"',
          '2014-02-13 13:50:00": "7.0"',
          '2014-02-13 06:00:00": "2"',
          '2014-02-13 03:00:00": "3"',
          '2014-02-13 12:00:00": "4"',
          '2014-02-13 13:00:00": "5"',
        ],
        [
          '2014-02-14 04:50:00": "1.0"',
          '2014-02-14 09:50:00": "4.0"',
          '2014-02-14 12:20:00": "6.0"',
          '2014-02-14 09:00:00": "3"',
          '2014-02-14 06:00:00": "2"',
          '2014-02-14 03:00:00": "3"',
        ],
        [
          '2014-02-15 06:50:00": "4.0"',
          '2014-02-15 10:20:00": "6.0"',
          '2014-02-15 06:00:00": "4"',
          '2014-02-15 06:20:00": "4.0"',
          '2014-02-15 06:20:00": "3"',
          '2014-02-15 03:00:00": "5"',
        ],
        [
          '2014-02-16 03:00:00": "5"',
          '2014-02-16 15:00:00": "5"',
          '2014-02-16 03:20:00": "6.0"',
          '2014-02-16 15:20:00": "5.0"',
          '2014-02-16 06:00:00": "2"',
          '2014-02-16 03:00:00": "4"',
        ],
        [
          '2014-02-17 01:00:00": "4"',
          '2014-02-17 11:50:00": "7.0"',
          '2014-02-17 22:00:00": "2"',
          '2014-02-17 23:50:00": "1.0"',
          '2014-02-17 06:00:00": "2"',
          '2014-02-17 05:00:00": "2"',
        ],
        [
          '2014-02-18 08:50:00": "5.0"',
          '2014-02-18 05:50:00": "3.0"',
          '2014-02-18 14:00:00": "6"',
          '2014-02-18 11:00:00": "6"',
          '2014-02-18 13:00:00": "4"',
          '2014-02-18 15:00:00": "2"',
        ]
      ],
      cur: 0, //默认选中第一个tab
    }
  },
  mounted() {
    this.getTimer();
  },
  methods: {
    getTimer() {
      this.timer = setInterval(() => {
        this.cur++;
        if (this.cur == this.tabTitle.length) {
          this.cur = 0;
        }
      }, 2000)
    },
    handleMouseOver(index) {
      this.cur = index;
      clearInterval(this.timer);
    },
    handleMouseOut(index) {
      this.getTimer();
    }
  },
  beforeDestroy() {
    clearInterval(this.timer);
  }
};
</script>

<style lang="scss" scoped>
.history-container {

  margin: 0 0.125rem;
  transform: scale(1.3); /* 调整整个图表的放大倍数 */
  .tabs {
    display: flex;
    .tab-tilte {
      li {
        color: #fff;
        background-color: rgba(36, 196, 255, 0.5);
        text-align: center;
        cursor: pointer;
        font-size: 0.125rem;
        width: 1.0rem;
        height: 0.35rem;
        line-height: 0.35rem;
        margin-bottom: 0.175rem;
        -webkit-border-radius: 5px;
        -ms-border-radius: 5px;
        -o-border-radius: 5px;
        -moz-border-radius: 5px;
        border-radius: 5px;
        &.active{
          background: linear-gradient(to right, #1b81bc, 20%, #24c4ff);
          color: #fff;
        }
      }
    }
    .indicatorDots {
      background-color: rgba(36, 196, 255, 0.5);
      width: 1px;
      height: 2.8rem;
      margin: 0.0625rem 0 0 0.375rem;
      margin-top :0.46rem;
      span {
        display: block;
        height: 0.525rem;
        margin-left: -0.0875rem;
        &:after {
          content: '';
          display: block;
          width: 0.125rem;
          height: 0.125rem;
          background: #ddd;
          -webkit-border-radius: 50%;
          -ms-border-radius: 50%;
          -o-border-radius: 50%;
          -moz-border-radius: 50%;
          border-radius: 50%;
          border: 2px solid #1b81bc;
        }
        &.active {
          &:after {
            background: #24c4ff;
            -webkit-box-shadow: 0 0 0.125rem #1b81bc;
            box-shadow: 0 0 0.125rem #1b81bc;
          }
        }
      }
    }
    .tab-content {
      display: flex;
      align-items: center;
      div {
        margin-left: 0.1875rem;
        color: #fff;
        .content {
          font-size: 0.175rem;
          line-height: 0.275rem;
          padding: 0.1rem 0;
        }
      }
    }
  }
}
</style>
