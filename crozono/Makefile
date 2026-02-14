PORTNAME=	crozono
DISTVERSION=	5.6a51669
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular framework designed to automate the penetration testing of wireless networks from drones and such unconventional devices.
WWW=		https://github.com/crozono/crozono-free

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/py-colorama@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-poormanslogging@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
