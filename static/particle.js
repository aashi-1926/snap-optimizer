tsParticles.load("tsparticles", {
    fullScreen: {
        enable: true,
        zIndex: -10
    },

    background: {
        color: "#0B0F14"
    },

    particles: {

        number: {
            value: 80
        },

        color: {
            value: [
                "#8FE3CF",
                "#C4F1BE",
                "#A7F3D0",
                "#E2F3F5"
            ]
        },

        links: {
            enable: true,
            distance: 140,
            color: "#7ED9B7",
            opacity: 0.15,
            width: 1
        },

        move: {
            enable: true,
            speed: 1
        },

        opacity: {
            value: 0.5
        },

        size: {
            value: {
                min: 2,
                max: 5
            }
        }
    }
});