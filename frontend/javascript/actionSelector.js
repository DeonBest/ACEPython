function handleRepsChange(actionKey, actionName) {
    const reps = parseInt(
      document.getElementById(`action-reps-${actionKey}`).value
    );
    // If already added, update its reps, otherwise ignore
    var actions = collectionConfig.actions;
    if (actions.some((action) => action.name === actionName)) {
      var actions = collectionConfig.actions;
      actions = actions.map((action) => {
        if (action.name === actionName) {
          return { ...action, reps };
        }
        return action;
      });
      collectionConfig.actions = actions;
    }
  }
  function handleActionSelection(actionKey, actionName) {
    const checked = document.getElementById(actionKey).checked;
    console.log(checked);

    const reps = parseInt(
      document.getElementById(`action-reps-${actionKey}`).value
    );
    var actions = collectionConfig.actions;
    if (actions.some((action) => action.name === actionName)) {
      actions = actions.filter(function (action) {
        return action.name !== actionName;
      });
    } else {
      if (reps == 0) {
        document.getElementById(`action-reps-${actionKey}`).value = 1;
      }
      actions.push({
        name: actionName,
        key: actionKey,
        reps: reps == 0 ? 1 : reps,
      });
    }
    collectionConfig.actions = actions;
    console.log(actions);
  }
  $(function () {
    fetch("http://127.0.0.1:5000/actions")
      .then((response) => response.json())
      .then((result) => {
        console.log("R", result);
        result.map((action) => {
          $("#list").append(`
              <li class="list-group-item">
                <div class="action-list-item">
                  <div class="action-list-field-sm">
                    <input
                      type="checkbox"
                      onclick="handleActionSelection('${action.action_key}','${action.action_name}')"
                      id="${action.action_key}"
                      value="${action.action_name}"
                    />
                  </div>
                  <div class="action-list-field-lg">${action.action_name}</div>
                  <div class="action-list-field-md">
                    <input
                      type="number"
                      class="form-control form-control-sm"
                      value=0
                      id="action-reps-${action.action_key}"
                      aria-describedby="repsIn"
                      onchange="handleRepsChange('${action.action_key}','${action.action_name}')"
                    />
                  </div>
                  <div class="action-list-field-md">
                    <div
                      style="display:flex;justify-content:center"
                      type="number"
                      id="action-status-${action.action_key}"
                      aria-describedby="actionStatus"

                      >
0
                    </div>
                  </div>
                </div>
              </li>
        `);
        });
      });
  });