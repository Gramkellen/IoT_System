<template>
  <div class="brand-container">
  	<div class="wrap">
      <header>
        <h2>某区域温度/湿度/气压数据发布订阅及分析处理系统</h2>
      </header>

      <section class="mainbox">
        <div class="item left">
          <div class="panel">
            <h2>一周湿度对比</h2>
            <stress></stress>
            <div class="panel-footer"></div>
          </div>

          <div class="panel">
            <h2>一周最高/最低温度</h2>
            <temp ></temp>>
            <div class="panel-footer"></div>
          </div>
          
        </div>

        <div class="item center">
          <div class="resume">
            <div class="resume-hd"> 
              <ul>
                <li>
                  <count-to :startVal="0" :endVal="600" :duration="3100"></count-to>
                </li>
                <li>
                  <count-to :startVal="0" :endVal="780" :duration="3100"></count-to>
                </li>
                <li>
                  <count-to :startVal="0" :endVal="700" :duration="3100"></count-to>
                </li>
              </ul>
            </div>
            <div class="resume-bd">
              <ul>
                <li>温度数据</li>
                <li>湿度数据</li>
                <li>气压数据</li>
              </ul> 
            </div>
          </div>
          <div class="panelx">
            <h2>温湿度/气压复合图</h2>
            <line1></line1 >
            <div class="panel-footer"></div>
          </div>
        </div>

        <div class="item right">
          <div class="panel">
            <h2>温湿度仪表盘</h2>
            <dash />
            <div class="panel-footer"></div>
          </div>
          
          <div class="panel">
            <h2>温度数据上传记录</h2>
            <history />
            <div class="panel-footer"></div>
          </div>
        </div>
      </section>
  
    </div>
    
  </div>
</template>

<script >
import '@/assets/js/flexible'
import stress from '@/components/DataView/stress.vue'
import history from '@/components/DataView/history.vue'
import temp from '@/components/DataView/temp.vue'
import dash from '@/components/DataView/dash.vue'
import line1 from '@/components/DataView/line1.vue'
import { CountTo } from 'vue3-count-to';
import * as echarts from 'echarts';
export default {
  name: 'dataview',
  components: { 
    CountTo,
    stress,
    history,
    temp,
    dash,
    line1,

     },
  data() {
  	return {
      imgSrc: '',
  	}
  },
  
}
</script>

<style lang="scss" scoped>
.brand-container {
  position: absolute;
  width: 100vw;
  height: 100vh;
  background-color: rgba(57, 105, 137, 0.5);
  .wrap {
    background-color: rgba(0, 0, 0, 0.0); 
    background-size: cover;
    line-height: 1.25;
    height: 100vh;
    header {
      position: relative;
      height: 1rem;
      width: auto;
      background: url(../assets/img/brand/head_bg.png) no-repeat top center;
      background-size: 100% 100%;
      h2 {
        color: #0d80b5;
        font-size: 0.475rem;
        text-align: center;
        line-height: 0.75rem;
        letter-spacing: 1px;
      }
    }
    
    .mainbox {
      height: 640px;
      min-width: 960px;
      max-width: 1235px;
      padding: 0.125rem 0.125rem 0;
      display: flex;
      background: rgba(0, 0, 0, 0.1);
      .item {
        flex: 3;
        &.center {
          flex: 4;
          margin: 0 0.125rem 0.1rem;
          overflow: hidden;

          .resume {
            background: rgba(101, 132, 226, 0.1);
            padding: 0.1875rem;
            .resume-hd {
              position: relative;
              border: 1px solid rgba(25, 186, 139, 0.17);
              ul {
                display: flex;
                %li-line {
                  content: "";
                  position: absolute;
                  height: 50%;
                  width: 1px;
                  background: rgba(255, 255, 255, 0.2);
                  top: 25%;
                }
                li {
                  position: relative;
                  flex: 1;
                  text-align: center;
                  height: 1.2rem;
                  line-height: 1.2rem;
                  font-size: 0.65rem;
                  color: #42b9da;
                  padding: 0.05rem 0;
                  font-family: 'DIGITALDREAMFAT';
                  font-weight: bold;
                  &:nth-child(2) {
                    &:after {
                      @extend %li-line;
                      right: 0;
                    }
                    &:before {
                      @extend %li-line;
                      left: 0;
                    }
                  }
                }
              }
              &:before {
                content: "";
                position: absolute;
                width: 30px;
                height: 10px;
                border-top: 2px solid #02a6b5;
                border-left: 2px solid #02a6b5;
                top: 0;
                left: 0;
              }
              &:after {
                content: "";
                position: absolute;
                width: 30px;
                height: 10px;
                border-bottom: 2px solid #02a6b5;
                border-right: 2px solid #02a6b5;
                right: 0;
                bottom: 0;
              }
            }
            .resume-bd {
              ul {
                display: flex;
                li {
                  flex: 1;
                  height: 0.1rem;
                  line-height: 0.1rem;
                  text-align: center;
                  font-size: 0.225rem;
                  color: rgba(255, 255, 255, 0.7);
                  //padding-top: 0.125rem;
                }
              }
            }
          }
        }
      }

    }

   
    .panel {
          position: relative;
          height: 5rem;
          border: 1px solid rgba(25, 186, 139, 0.17);
          background: rgba(255, 255, 255, 0.04) url(../assets/img/brand/line.png);
          padding: 0 0.1875rem 0;
          margin-bottom: 0.1875rem;
          &:before {
            position: absolute;
            top: 0;
            left: 0;
            content: "";
            width: 10px;
            height: 10px;
            border-top: 2px solid #02a6b5;
            border-left: 2px solid #02a6b5;
          }
          &:after {
            position: absolute;
            top: 0;
            right: 0;
            content: "";
            width: 10px;
            height: 10px;
            border-top: 2px solid #02a6b5;
            border-right: 2px solid #02a6b5;
          }

          .panel-footer {
            position: absolute;
            left: 0;
            bottom: 0;
            width: 100%;
            &:before {
              position: absolute;
              bottom: 0;
              left: 0;
              content: "";
              width: 10px;
              height: 10px;
              border-bottom: 2px solid #02a6b5;
              border-left: 2px solid #02a6b5;
            }
            &:after {
              position: absolute;
              bottom: 0;
              right: 0;
              content: "";
              width: 10px;
              height: 10px;
              border-bottom: 2px solid #02a6b5;
              border-right: 2px solid #02a6b5;
            }
          }

          h2 {
            height: 0.6rem;
            line-height: 0.6rem;
            text-align: center;
            color: #fff;
            font-size: 0.225rem;
            font-weight: 400;
            a {
              margin: 0 0.1875rem;
              color: #fff;
              text-decoration: none;
            }
          }
          .chart {
            height: 6rem;
          }
        }
        .panelx {
          position: relative;
          height: 54.7vh;
          border: 1px solid rgba(25, 186, 139, 0.17);
          background: rgba(255, 255, 255, 0.04) url(../assets/img/brand/line.png);
          padding: 0 0.1875rem 0;
          margin-bottom: 0.1875rem;
          &:before {
            position: absolute;
            top: 0;
            left: 0;
            content: "";
            width: 10px;
            height: 10px;
            border-top: 2px solid #02a6b5;
            border-left: 2px solid #02a6b5;
          }
          &:after {
            position: absolute;
            top: 0;
            right: 0;
            content: "";
            width: 10px;
            height: 10px;
            border-top: 2px solid #02a6b5;
            border-right: 2px solid #02a6b5;
          }

          .panel-footer {
            position: absolute;
            left: 0;
            bottom: 0;
            width: 100%;
            &:before {
              position: absolute;
              bottom: 0;
              left: 0;
              content: "";
              width: 10px;
              height: 10px;
              border-bottom: 2px solid #02a6b5;
              border-left: 2px solid #02a6b5;
            }
            &:after {
              position: absolute;
              bottom: 0;
              right: 0;
              content: "";
              width: 10px;
              height: 10px;
              border-bottom: 2px solid #02a6b5;
              border-right: 2px solid #02a6b5;
            }
          }

          h2 {
            height: 0.6rem;
            line-height: 0.6rem;
            text-align: center;
            color: #fff;
            font-size: 0.225rem;
            font-weight: 400;
            a {
              margin: 0 0.1875rem;
              color: #fff;
              text-decoration: none;
            }
          }
          .chart {
            height: 45vh;
          }
        }



  }

}
</style>
