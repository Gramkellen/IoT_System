import Mock from 'mockjs'

// 是否使用mock.js模拟数据
// let useMock = true
let useMock = true;
if (useMock) {
    Mock.mock('/weathersystem/subscribe/', 'post',(options) =>{         //三个主题订阅状态
        console.log(options.body);
        return{
        };
    })

    Mock.mock('/weathersystem/history/', 'post',(options) =>{         //保存历史记录
        console.log(options.body);
        return{
        };
    })

    Mock.mock(/weathersystem\?user=.*/, 'get',{

    });

}

export default Mock