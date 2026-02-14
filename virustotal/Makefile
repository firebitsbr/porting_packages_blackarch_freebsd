PORTNAME=	virustotal
DISTVERSION=	4.9aea023
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Command-line utility to automatically lookup on VirusTotal all files recursively contained in a directory.
WWW=		https://github.com/botherder/virustotal

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-simplejson@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
