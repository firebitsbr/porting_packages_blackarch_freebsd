PORTNAME=	usb-canary
DISTVERSION=	31.bb23552
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Linux or OSX tool that uses psutil to monitor devices while your computer is locked. In the case it detects someone plugging in or unplugging devices it can be configured to send you an SMS or alert you via Slack or Pushover.
WWW=		https://github.com/errbufferoverfl/usb-canary

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		devel/git

RUN_DEPENDS=	??/py-virtualenv@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
