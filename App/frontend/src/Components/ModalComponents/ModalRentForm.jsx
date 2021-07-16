import React, { useState } from "react";

export const ModalCreate = (props) => {
  const [showInfo, setShow] = useState(false);
  const [phone, setPhone] = useState("");
  const [startDate, setDate] = useState("");
  return (
    <>
      <form
        onSubmit={(e) => {
          console.log(phone);
          e.preventDefault();
        }}
      >
        <div>
          Start Date:
          <input type="date" />
        </div>
        <div>
          End Date:
          <input type="date" />
        </div>
        <div>
          Renter's Phone
          <input
            id="telNo"
            name="telNo"
            type="tel"
            required
            pattern="[0-9]{11}"
            placeholder="17789527551"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
          <span class="validity"></span>
        </div>
        <div>
          Mile limits:
          <input type="number" />
        </div>
        <button>Submit</button>
      </form>
    </>
  );
};
