PORTNAME=	uncaptcha2
DISTVERSION=	7.473f33d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Defeating the latest version of ReCaptcha with 91% accuracy.
WWW=		http://uncaptcha.cs.umd.edu/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pyautogui@${PY_FLAVOR} \
		??/py-speechrecognition@${PY_FLAVOR} \
		??/py-xlib@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
