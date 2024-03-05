var fill = document.getElementById('store');
var flagstar = false;// flagstar从数据库中获得

var only = document.getElementById('topic');
var flagonly = false;

// 收藏功能
fill.addEventListener('click',function(){
    if(flagstar)
        {
            // 若已收藏，则变为收藏并 传递取消收藏请求（待完成）
            fill.style.backgroundImage = 'url(/static/images/store.png)';
            flagstar = false;
        }else{
            // 若没收藏，则变为收藏并 传递收藏请求（待完成）
            fill.style.backgroundImage = 'url(/static/images/store_fill.png)';
            flagstar = true;
        }
});

// 转发分享功能

// 只看楼主
only.addEventListener('click',function(){
    if(flagonly)
        {
            // 看全部帖
            only.className='topic_top'
            flagonly = false;
        }else{
            // 只看楼主（待完成）
            only.className='topic_tap'
            flagonly = true;
        }
});

