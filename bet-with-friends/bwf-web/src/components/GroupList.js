import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getGroups } from "./servicees/groupServices";

const GroupList = () => {
  const [groups, setGroups] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);

  useEffect(() => {
    setLoading(true);
    const getData = async () => {
      await getGroups()
        .then((data) => {
          setGroups(data);
          setLoading(false);
        })
        .catch((e) => {
          setError(true);
          setLoading(false);
        });

      // try {
      //  const resp = await axios.get("http://127.0.0.1:8000/api/groups/")
      //  console.log(resp.data)
      // } catch (error) {
      //   console.error(error)
      // }
    };
    getData();
  }, []);

  if (error) return <h1>Error</h1>;
  if (loading) return <h1>Loading...</h1>;

  return (
    <div className='App'>
      <header className='App-header'>
        {groups &&
          groups.map((group) => {
            return (
              <Link key={group.id} to={`/details/${group.id}`}>
                {/* Key in the map should be in top level element */}
                <p>
                  {group.name}: {group.location}
                </p>
              </Link>
            );
          })}
      </header>
    </div>
  );
};

export default GroupList;
