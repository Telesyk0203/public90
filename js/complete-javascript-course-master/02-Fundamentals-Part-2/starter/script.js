'use strict'

// let hasDriverLicense = false;
// const passTest = true ;

// if (passTest) haseDroiverLicense = true;
// if(hasDriverLicense) console.log("I!!!");

// function fruitProcessor(apple, oranges) {
//       const juice = `Juice with ${apple} apples and ${oranges} oranges!!!`
//       return juice
// }
// const my_choice = fruitProcessor(1, 3)
// console.log(my_choice)
// console.log(fruitProcessor(7, 3))

// function calcAge1(birthYear) {
//       return 2037 - birthYear
// }
// const age = calcAge1(1990)
// console.log(age)

// const calcAge2 = function (birthYear) {
//       return 2037 - birthYear
// }

// const age2 = calcAge2(1991)

//Arrow function

// const calcAge3 = (birthYear) => 2037 - birthYear
// const age3 = calcAge3(1991)
// console.log(age3)

// const retir = (birthYear, firstname) => {
//       const age = 2037 - birthYear
//       const retirement = 65 - age
//       return `${firstname} retiers in ${retirement}`
// }
// console.log(retir(1990, 'Taras'))
// console.log(retir(1991, 'Ksu'))

// const calcAge = function (birthYear) {
//       return 2037 - birthYear
// }

// const retir = function (birthYear, firstname) {
//       const age = calcAge(birthYear)
//       const retirement = 65 - age

//       console.log(`${firstname} retiers in ${retirement}`)
//       if (retirement > 0) {
//             return retirement
//       } else {
//             console.log(`${firstname} has already retired 🎉🎉🎉🎉🎉`)
//             return -1
//       }
//       // return `${firstname} retiers in ${retirement}`
// }

// console.log(retir(1990, 'Taras'))
// console.log(retir(1970, 'Oleg'))

// Chalandge #1
// const calcAverage = function (_1_GameScore, _2_GameScore, _3_GameScore) {
//       const averageScore = (_1_GameScore + _2_GameScore + _3_GameScore) / 3
//       return averageScore
// }
// const avgDolphins = calcAverage(85, 54, 41)
// const avgKoalas = calcAverage(23, 34, 27)

// console.log(
//       `Average scores Dolphins🐬 is ${avgDolphins} points & average scores Koalas🐨 is ${avgKoalas} points !!! `
// )

// const checkWinner = function (avgDolphins, avgKoalas) {
//       if (avgDolphins >= 2 * avgKoalas) {
//             return console.log(
//                   `Dolphins🐬 win 🏆 (${avgDolphins} vs. ${avgKoalas})`
//             )
//       } else if (avgKoalas >= 2 * avgDolphins) {
//             return console.log(
//                   `Koalas🐨 win 🏆 (${avgKoalas} vs. ${avgDolphins})`
//             )
//       } else {
//             console.log(`Anyone wins the 🏆😒😒😒😒 `)
//       }
// }

// checkWinner(avgDolphins, avgKoalas)

// const friends = ['Taras', 'Oksana', 'Iryna', 'Vlad']

// const year = new Array(1990, 1991, 1995, 1994)

// console.log(friends[2])
// console.log(friends.length)
// console.log(friends[friends.length - 1])

// friends[2] = 'Daryna'

// console.log(friends)
// const firstName = 'Taras'
// const secondName = 'Strikha'
// const birthyear = 1990
// const profesion = 'programmer'
// const taras = [firstName, secondName, birthyear, profesion, friends]

// console.log(taras)
// console.log(taras.length)

// // Exercise

// const calcAge = function (birthYear) {
//     return 2022 - birthYear
// }

// const age1 = calcAge(year[0])
// const age2 = calcAge(year[1])
// const age3 = calcAge(year[2])
// const age4 = calcAge(year[3])

// console.log(age1, age2, age3, age4)

// const ages = [age1, calcAge(year[1]), age3, age4]
// console.log(ages)

// const friends = ['Taras', 'Oksana', 'Iryna', 'Vlad']
// //Add elements
// const newfriends = friends.push('Nataly')
// console.log(friends)

// friends.unshift('Alex')
// console.log(friends)
// // Remove elements
// const popped = friends.pop() //last
// console.log(popped)
// console.log(friends)

// friends.shift() //first elements ;
// console.log(friends)

// console.log(friends.indexOf('Taras'))
// console.log(friends.indexOf('Bob'))

// console.log(friends.includes('Taras'))
// console.log(friends.includes('Bob'))

// if (friends.includes('Vlad')) {
//     console.log('You have a friend called Vlad')
// }

//Challenge #3
// const calcTip = function (bill) {
//     if (bill > 50 && bill < 300) {
//         const tip = bill * 0.15
//         return tip
//     } else {
//         const tip = bill * 0.2
//         return tip
//     }
// }
// console.log(calcTip(100))

// const bills = [125, 555, 44]
// console.log(bills)

// const tips = [calcTip(bills[0]), calcTip(bills[1]), calcTip(bills[2])]
// console.log(tips)

// const total = [bills[0] + tips[0], bills[1] + tips[1], bills[2] + tips[2]]
// console.log(total)

// const tarasArray = [
//     'Taras',
//     'Strikha',
//     1990,
//     'military',
//     ['Oksana', 'Iryna', 'Vlad'],
// ]

// const taras = {
//     firstName: 'Taras',
//     lastName: 'Strikha',
//     age: 2022 - 1990,
//     job: 'military',
//     friends: ['Oksana', 'Iryna', 'Vlad'],
// }
// console.log(taras)

// console.log(taras.lastName)
// console.log(taras['lastName'])

// const nameKey = 'Name'
// console.log(taras['first' + nameKey])
// console.log(taras['last' + nameKey])

// const interestedID = prompt('what do you want about Taras ? Choose between firstName, lastName , age, job and friends ');
//       if (taras[interestedID]){
//             console.log(taras[interestedID]);

//       }else{
//             console.log('Wrong request!Choose between firstName, lastName , age, job and friends')
//       };

// taras.location = 'Poltava';
// taras['twitter'] = '@t.strikha90';


// // Challenge 
// //Taras has 3 friends , and his best friend is called Oksana

// // taras.bestFriend = taras.friends[0];

// console.log(`${taras.firstName} has ${taras.friends.length} friends, and the best friend is ${taras.friends[0]}❤️!!!`);


// const taras = {
//       firstName: 'Taras',
//       lastName: 'Strikha',
//       birthYear: 1990,
//       job: 'military',
//       friends: ['Oksana', 'Iryna', 'Vlad'],
//       hasDriverLicense : false,

//       // calcAge : function (birthYear) {
//       //    return 2022 - birthYear;   
//       // }

//       // calcAge : function () {
//       //       // console.log(this);
//       //       return 2022 - this.birthYear;   
//       //    }

//       calcAge : function () {
//             this.age = 2022 - this.birthYear;
//             return this.age;   
//          },
      
//       getSummary : function (){
//           return `${this.firstName} is a ${this.calcAge()}-years old  ${this.job} , and ${this.hasDriverLicense ? "has a driver's license" : "has'NOT a driver's license"}!!`
//       }
//  };


// console.log(taras.calcAge());

// console.log(taras.age);
// console.log(taras.age);
// console.log(taras.age);
// console.log(taras.age);
// console.log(taras['calcAge'](1990));
//Challenge
//"Taras is a 32-year old military , and he has a driver's license "

// if (this.hasDriverLicense=== true) {
//       const driverLicense = "has a driver's license";
// } else{
//       const driverLicense = "has'NOT a driver's license";
// };
// taras.hasDriverLicense();
// console.log (taras.getSummary());


const mark = {
      firstName: 'Mark',
      lastName : 'Miller',
      mass : 78 ,
      hight : 1.69,
      calcBMI : function (){
            this.bmi = this.mass /this.hight ** 2 ;
            return this.bmi
      },
}

console.log(mark.calcBMI())

const john = {
      firstName: 'John',
      lastName : 'Smith',
      mass : 92 ,
      hight : 1.95,
      calcBMI : function (){
            this.bmi = this.mass /this.hight ** 2 ;
            return this.bmi
      },
}


console.log(john.calcBMI());

if (mark.bmi > john.bmi){

      console.log(`${mark.firstName} ${mark.lastName} bmi (${mark.bmi}) is higher than ${john.firstName} ${john.lastName} bmi (${john.calcBMI()})`)
}else{
      console.log(`${mark.firstName} ${mark.lastName} bmi (${mark.bmi}) is NOT higher than ${john.firstName} ${john.lastName} bmi (${john.calcBMI()})`)

}