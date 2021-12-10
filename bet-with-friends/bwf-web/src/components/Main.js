import React from "react";
import GroupList from "./GroupList";
import { Switch, Route } from "react-router-dom";
import GroupDetails from "./GroupDetails";

const Main = () => {
  return (
    <div className='main'>
      <Switch>
        <Route exact path='/'>
          <GroupList />
        </Route>
        <Route path='/details/:id'>
          <GroupDetails />
        </Route>
      </Switch>
    </div>
  );
};

export default Main;
