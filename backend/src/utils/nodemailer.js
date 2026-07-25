import nodemailer from 'nodemailer'


export const nodemailerService = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 465,
    secure: true,
    auth : {
        user : process.env.MAIL,
        pass : process.env.APP_PASS
    }
})