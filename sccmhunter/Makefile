PORTNAME=	sccmhunter
DISTVERSION=	v.1.1.11.r12.g2f2e47f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Identifying, profiling, and attacking SCCM related assets in an Active Directory domain.
WWW=		https://github.com/garrettfoster13/sccmhunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket-ba \
		??/py-cmd2@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		??/py-requests-toolbelt@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-typer@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
