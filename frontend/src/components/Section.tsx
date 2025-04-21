import { FC, PropsWithChildren } from "react";
import { Stack, Divider } from "@mui/material";
import { Subtitle } from "./Subtitle";

interface SectionProps {
  title?: string;
}

export const Section: FC<PropsWithChildren<SectionProps>> = ({ children, title }) => {
  return (
    <Stack direction="column" spacing={2}>
      {title && <Subtitle>{title}</Subtitle>}
      <Stack direction="row" spacing={2}>
        {children}
      </Stack>
      <Divider />
    </Stack>
  );
};
