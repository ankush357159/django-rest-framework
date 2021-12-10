import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { useFetchGroup } from "./hooks/fetch-group";
import { DateTime } from "luxon";
import CalendarTodayIcon from "@mui/icons-material/CalendarToday";
import AccessTimeIcon from "@mui/icons-material/AccessTime";
import { makeStyles } from "@mui/styles";

const useStyles = makeStyles(theme => ({
  dateTime: {
    fontSize: "18px",
    marginRight: "3px",
    marginTop: "10px",
    color: theme.colors.mainAccentColor
  },
}));

const GroupDetails = () => {
  const classes = useStyles();
  const { id } = useParams();
  const [data, loading, error] = useFetchGroup(id);
  const [group, setGroup] = useState(null);

  useEffect(() => {
    setGroup(data);
  }, [data]);
  if (error) return <h1>Error</h1>;
  if (loading) return <h1>Loading...</h1>;

  return (
    <div>
      <Link to='/'>Back</Link>
      {group && (
        <React.Fragment>
          <h1>
            {group.name} {group.location}
          </h1>
          <h1>{group.description}</h1>

          <h3>Events:</h3>
          {group.events.map((event) => {
            const format = "yyyy-MM-dd'T'HH:mm:ss'Z'";
            const evtTime = DateTime.fromFormat(event.time, format);
            return (
              <div key={event.id}>
                <div>
                  {event.team1} VS {event.team2}
                  <p>
                    <CalendarTodayIcon className={classes.dateTime}/>
                    {evtTime.toSQLDate()} <AccessTimeIcon className={classes.dateTime}/>
                    {evtTime.toFormat("HH:mm")}
                  </p>
                </div>
              </div>
            );
          })}
        </React.Fragment>
      )}
    </div>
  );
};

export default GroupDetails;
