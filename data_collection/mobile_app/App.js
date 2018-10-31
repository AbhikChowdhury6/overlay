import React, {Component} from 'react';
import {StyleSheet, Text, View, ScrollView, TextInput} from 'react-native';
import { createStackNavigator, createDrawerNavigator} from 'react-navigation';

import InfoScreen from './components/screens/infoPage';
import MoodScreen from './components/screens/moodPage';
import HamburgerMenu from './components/hamburgermenu';
import Header from './components/header';
import HomeScreen from './components/screens/home';

var navOptions = {
  headerTitleStyle: {
    width: '100%',
    flex: 1,
    textAlign: 'center',
  }
}

const HomeStack = createStackNavigator(
  {
    Home: {
      screen: HomeScreen,
    }
  },
  {
    initialRouteName: 'Home',
    navigationOptions: navOptions,
  }
);

const InfoStack = createStackNavigator(
  {
    Info: {
      screen: InfoScreen,
    }
  },
  {
    initialRouteName: 'Info',
    navigationOptions: navOptions,
  }
);

const MoodStack = createStackNavigator(
  {
    Mood: {
      screen: MoodScreen,
    }
  },
  {
    initialRouteName: 'Mood',
    navigationOptions: navOptions,
  }
);

const RootStack = createDrawerNavigator(
    {
      Home: {
        screen: HomeStack,
      },
      Info: {
        screen: InfoStack,
      },
      Mood: {
        screen: MoodStack,
      },
    },
    {
      initialRouteName: 'Home',
      drawerPosition: 'left',
      drawerWidth: 300,
      contentComponent: HamburgerMenu
    }
);

export default class App extends React.Component {
  render() {
    return(
      <RootStack/>
    );
  }
}
