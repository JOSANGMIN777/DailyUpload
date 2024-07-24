// 엘리스 SW 엔지니어 3,6,9 문제

for (var i = 1; i <= 30; i++) {
  var flag = false;
  for (var j = 0; j < i.toString().length; j++) {
    if (
      i.toString()[j] === '3' ||
      i.toString()[j] === '6' ||
      i.toString()[j] === '9'
    ) {
      flag = true;
      break
    }
  }
    if (flag) {
      console.log('짝!');
    }else {
    console.log(i);
  }
}

// 이 문제는 진짜 지랄맞다. 아니 그냥 js는 뭔가 이상해 뭔가 다 억까야 그냥 어쨌든 풀어냈다. 취업도 풀어내자 이처럼