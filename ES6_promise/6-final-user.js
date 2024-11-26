import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName).then((value) => ({
    status: 'fulfilled',
    value,
  }));

  const uploadPhotoPromise = uploadPhoto(fileName).catch((error) => ({
    status: 'rejected',
    value: error.toString(),
  }));

  return Promise.allSettled([signUpPromise, uploadPhotoPromise]);
}
