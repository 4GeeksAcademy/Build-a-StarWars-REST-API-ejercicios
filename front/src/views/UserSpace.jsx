import { Dashboard } from "../components/Dashboard";
import { NeedValidation } from "../components/NeedValidation";

export const UserSpace = () => {
  return (
    <NeedValidation>
      <Dashboard />
    </NeedValidation>
  );
};
