 
// let js = 'amazing';
//       if (js=== 'amazing') alert ('JavaScript is FUN !');
//      40+8+23-10;
// console.log(40+8+23-10) ;

// let country = 'Ukraine' ;
// let continent = 'Europe';
// let population = '40 millions';
// // console.log(country);
// // console.log(continent);
// // console.log(population);

// // Variable  name conventions

// // let jonas_matilda = 'JM';
// // let $function= 27 ;

// // let person = 'jonas';
// // let PI = 3.1415;

// // let myFirstJob= 'Military serviceman';
// // let myFutureJob = 'Devops';

// // console.log(myFirstJob);

// // let JavaScriptIsFun = true;
// // console.log(JavaScriptIsFun);

// // // console.log(typeof true);
// //console.log(typeof JavaScriptIsFun );
// // // console.log(typeof 'TAras');
// // // console.log(typeof 25) ;
// // JavaScriptIsFun = 'YES!!!'
// // console.log(typeof JavaScriptIsFun);

// // let year;
// // console.log(year);
// // console.log(typeof year);
// // year = 1990;
// // console.log(typeof year);

// // let isIsland = false;
// // let language ;

// // console.log(typeof isIsland);
// // console.log(typeof country);
// // console.log(typeof population);
// // console.log(typeof language);

// // let age = 32;
// // age = 33 ;

// // const bithYear = 1990 ;
 
// // const MarksWeight = 78 ;
// // const MarksTall = 1.69;
// // const MarksBMI = MarksWeight / MarksTall  ** 2 ;
// // console.log(MarksBMI);

// // const JohnWeight = 92 ;
// // const JohnTall = 1.95 ; 
// // const JohnBMI = JohnWeight / (JohnTall * JohnTall) ; 
// // console.log(JohnBMI);

// // const markHigherBMI = MarksBMI > JohnBMI ; 
// // console.log(markHigherBMI);

// // const TarasWeihgt =  103 ;
// // const TarasTall = 1.86 ; 
// // const TarasBMI = TarasWeihgt / (TarasTall**2);
// // console.log('Taras BMI is ', TarasBMI); 

// // if (TarasBMI <= 18.5 ) {console.log(`Taras BMI is Underweight `)} else {console.log(`${TarasBMI} iqule to much!!!`)};
// // if (  18.5 <= TarasBMI >=24.9 ) {console.log('Taras BMI is Normal weight' )};
// // if ( 24.9 <= TarasBMI <= 24.9 ) {console.log('Taras BMI is Overweight' )};
// //  console.log(`Привіт 
// //  ${country} , 
// //  а твоя чисельність ${population} ?`)

// // if (MarksBMI > JohnBMI) {
// //     console.log(`   MarksBMI(${MarksBMI}) higher than JohnBMI(${JohnBMI})!!!!!`)
// // } else {  
// //     console.log(`    MarksBMI(${MarksBMI}) DON'T higher than JohnBMI(${JohnBMI})!!!!!`)
// // }

// //type conversion
// const inputYear = '1990';
// console.log(Number(inputYear), inputYear);
// console.log(inputYear + 18);
// console.log(Number(inputYear) + 18);
// console.log(Number('Taras'));// NaN
// console.log(typeof NaN);// number

// console.log(typeof String(23),  typeof 23);// string number

// // type coercion
// console.log('I am ' + 30 + ' years old!!!')// + ever make(converted number to string) string  
// console.log('I am ' + '30' + ' years old!!!')

// console.log('23'-'10' - 3);// - ever make(converted string to number) number
// console.log('23'-'10' + 3); // 16
// console.log('23'+'10' + 3); //23103
// console.log('23' * '123' ); //2829
// console.log('23'/'10'); //2.3

// let n = '1' + 1 ; //'11'
// n = n - 1 ; 
// console.log(n) ;

// n = 2+ 3+ 4  ; // 9
// n = n + '5'; 
// console.log(n) ;

// n = '12'-' 3'-' 4'  ; // 
// n = n + '5'; 
// console.log(n) ;

// 5 falsy values : 0 , undefined, null, NaN

// console.log(Boolean(0));//false
// console.log(Boolean(undefined));//false
// console.log(Boolean('Taras'));//true
// console.log(Boolean({}));//true
// console.log(Boolean(''));//false
// console.log(Boolean(NaN));//false


// const money = 0 ;
// if(money) {
//     console.log("Don't spend it all ;)");
// } else {
//     console.log("You should get a job !!!!!!!");
// }

// let hight;
// if(hight) {
//     console.log("YaY! Height is defined!!!");
// }else{
//     console.log("Height is UNDEFINED!!!!");
// }

// == vs ===  EQUALITY OPERATORS

// const age = "18" ;

// if (age === 18) console.log('You just became an adult!!!(strict)');// === compare and values and typeof date 

// if (age == 18) console.log('You just became an adult!!! (loose)');//== compare just values without typeof date 

// 18 === 18// true

// 18 =="18"//true

// 18 ==="18"//false


// const favorite = prompt("What's is your favorite number ? ") ;
// console.log(favorite);
// console.log(typeof favorite);

// if (favorite == 66) {console.log("YEEEP it's 66!!!");}
// else if (Number (favorite) === 66) {console.log("  66 not a NUMBER !!! IT'S Sting !!!")} 
// else if (favorite == 666) {console.log(`Cool! ${favorite} is your favorite number`)} else {
//     console.log(`${favorite} is number are not COOL !!!`);
// }

// if(favorite!== 666) console.log('Why not 666??');// !== not equal

// Booling logic 
 
// let age = 16 ;

// let a = age >= 20;
// let b = age < 30;

// console.log(!a);// not a 
// console.log(a && b);// a and b
// console.log(a || b);// a or b 

// const _1_DolphsScore =97 ;
// const _2_DolphScore = 112 ; 
// const _3_DolphScore = 101;
// const averageDolphinsScores = (_1_DolphsScore+_2_DolphScore+_3_DolphScore)/ 3;

// const _1_KoalasScore= 109;
// const _2_KoalasScore = 95 ;
// const _3_KoalasScore = 123;
// const avarageKoalasScores = (_1_KoalasScore+ _2_KoalasScore + _3_KoalasScore)/3;

// console.log(averageDolphinsScores , avarageKoalasScores);

// if (averageDolphinsScores > avarageKoalasScores) {
//     console.log("Dolphins WIN!!!!!");
// } else if  (avarageKoalasScores > averageDolphinsScores) {
// console.log("Koalas WIN!!!!!");
// } else {
//     console.log( " DRAW!!!!!")
// }
// console.log(_1_DolphsScore  >= 100 , _1_KoalasScore >= 100);
// if (_1_KoalasScore > 100 && _1_DolphsScore > 100) 
//     {
//          if (_1_DolphsScore > _1_KoalasScore )
//         { 
//             console.log("Dolphons WIN!!! First game !!! ")
//         } else if (_1_DolphsScore < _1_KoalasScore) 
//         {
//             console.log("Kaolas WON!!! FIRST game!!!")
//         } else if (_1_DolphsScore === _1_KoalasScore)
//         {
//             console.log("DRAW!!! FIRST GAME");
//         }
//      } else {
//                 console.log("FIRST GAME don't use all requirements!!!")
//                 };


//  console.log(_2_DolphScore  >= 100 , _2_KoalasScore >= 100)
//  if (_2_KoalasScore > 100 && _2_DolphScore > 100) 
                
// { if (_2_DolphScore > _2_KoalasScore )
//      { 
//                         console.log("Dolphons WIN!!! SECOND game !!! ")
                    
//     } else if (_2_DolphScore < _2_KoalasScore) 
//     {
//                         console.log("Kaolas WON!!! SECOND game!!!")
//      } else if (_2_DolphScore === _2_KoalasScore)
//     {
//                          console.log("DRAW!!! SECOND GAME");
//     }
// } else 
// {
//  console.log("SECOND GAME don't use all requirements!!!")
//  };
 
// console.log(_3_DolphScore  >= 100 , _3_KoalasScore >= 100);
// if (_3_KoalasScore > 100 && _3_DolphScore > 100) 
                
//          { if (_3_DolphScore > _3_KoalasScore )
//             { 
//                         console.log("Dolphons WIN!!! THIRD game !!!")
                    
//             } else if (_3_DolphScore < _3_KoalasScore) 
//             {
//                         console.log("Kaolas WON!!! THIRD game!!!")
//              } else if (_3_DolphScore === _3_KoalasScore)
//              {
//                          console.log("DRAW!!! THIRD GAME");
//                     }
//         } else 
//         {
//                  console.log("THIRD GAME don't use all requirements!!!")
//             };

// const day = prompt('Input one day of the week !!! And you wiil see yours plan on this DAY ! ');

// switch(day) {
//     case 'monday':
//         console.log('Plan course structure');
//         console.log('Go to coding meetup');
//         break;
//     case  'tuesday':
//         console.log('Prepare theory videos ))))');
//         break;
//     case 'wednesday':
//         console.log('Have some FUN!!!');
//         break;
//     // case 'thursday':
//     //     console.log('Write code examples');
//     //     break;
//     case 'friday':
//         console.log('Go to drink on the evening!');
//         break;
//     // case 'saturday':
//     //     console.log('Ride on the bicycle!!!');
//     //     break;
//     case 'sunday':
//         console.log('Have DAYOFF!!!');
// };

//  if (day === 'thursday') {
//     console.log('Write code examples');
//  } else if (day === 'saturday') {
//     console.log('Ride on the bicycle!!!');
//  };

// const age = prompt('Input your age!!!');

// // age >= 18 ? console.log('You can drink alcohol like 🍷, 🍺, 🍹') : console.log('You can drink just water 🚰');

// let drink = age >=18 ? "alcohol like 🍷, 🍺, 🍹" : 'just water 🚰';

// console.log(drink);
// console.log(`I like to drink ${age >=18 ? "alcohol like 🍷, 🍺, 🍹" : 'just water 🚰'}`);

const bill = prompt ('How much money did you spend ?');
const tip = 50<=bill<=300 ? (bill*15)/100 : (bill*20)/100 ;
const total = Number(bill) + Number(tip) ;

console.log( `The bill was ${bill}$, the tip was ${tip}$, and the total value ${total} $`)


