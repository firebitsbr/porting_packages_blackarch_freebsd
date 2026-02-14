PORTNAME=	koadic
DISTVERSION=	3.457f9a3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Windows post-exploitation rootkit similar to other penetration testing tools such as Meterpreter and Powershell Empire.
WWW=		https://github.com/offsecginger/koadic

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-flask@${PY_FLAVOR} \
		??/py-legacy-cgi@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-rjsmin@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
