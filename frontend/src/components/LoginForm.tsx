import { Stack, TextField, Button, Typography } from "@mui/material";
import { Formik, Form, FormikHelpers } from "formik";
import { useNavigate } from "react-router";
import * as yup from "yup";
import { useAuth } from "../contexts/auth";

interface FormValues {
  email: string;
  password: string;
}

const initialValues: FormValues = {
  email: "",
  password: "",
};

const validationSchema = yup.object({
  email: yup.string().email("Please enter a valid email address").required("Email is required"),
  password: yup.string().min(6, "Password must be at least 6 characters").required("Password is required"),
});

export const LoginForm = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (values: FormValues, { setSubmitting, setStatus }: FormikHelpers<FormValues>) => {
    try {
      await login(values.email, values.password);
      navigate("/");
    } catch {
      setStatus({ error: "Invalid email or password" });
    } finally {
      setSubmitting(false);
    }
  };

  const handleCancel = () => navigate("/");

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
      validateOnMount={false}
      validateOnChange={false}
      validateOnBlur={false}
    >
      {({ isSubmitting, touched, errors, handleChange, handleBlur, values, status }) => (
        <Form noValidate>
          <Stack spacing={2} alignItems="center">
            <Typography variant="h4" sx={{ fontWeight: "bold" }}>
              Sign in
            </Typography>
            {status ? (
              <Typography variant="subtitle1" color="error">
                {status.error}
              </Typography>
            ) : (
              <Typography variant="subtitle1" color="textSecondary">
                Welcome user, please sign in to continue
              </Typography>
            )}
            <TextField
              variant="outlined"
              label="Email"
              name="email"
              type="email"
              value={values.email}
              onChange={handleChange}
              onBlur={handleBlur}
              error={touched.email && !!errors.email}
              helperText={touched.email && errors.email}
              autoComplete="email"
              required
              fullWidth
            />
            <TextField
              variant="outlined"
              label="Password"
              name="password"
              type="password"
              value={values.password}
              onChange={handleChange}
              onBlur={handleBlur}
              error={touched.password && !!errors.password}
              helperText={touched.password && errors.password}
              autoComplete="current-password"
              required
              fullWidth
            />
            <Button type="submit" variant="contained" size="large" fullWidth disabled={isSubmitting}>
              {isSubmitting ? "Signing in..." : "Sign in"}
            </Button>
            <Button variant="contained" size="large" fullWidth onClick={handleCancel}>
              Cancel
            </Button>
          </Stack>
        </Form>
      )}
    </Formik>
  );
};
